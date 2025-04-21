import pickle
import hashlib
from typing import Any, Callable, Iterator, Optional, Tuple, TypeVar, Generic

KT = TypeVar('KT') 
VT = TypeVar('VT') 

class Node(Generic[KT, VT]):
    def __init__(self, key: KT, value: VT, next: Optional['Node']=None):
        self.key = key
        self.value = value
        self.next = next

class LinkedList(Generic[KT, VT]):
    def __init__(self):
        self.head: Optional[Node[KT, VT]] = None

    def append(self, key: KT, value: VT) -> None:
        if self.head is None:
            self.head = Node(key, value)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(key, value)

    def find(self, key: KT) -> Optional[Node[KT, VT]]:
        current = self.head
        while current is not None:
            if current.key == key:
                return current
            current = current.next
        return None

    def remove(self, key: KT) -> bool:
        current = self.head
        prev = None
        while current is not None:
            if current.key == key:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next
        return False

    def __iter__(self) -> Iterator[Node[KT, VT]]:
        current = self.head
        while current is not None:
            yield current
            current = current.next

class HashMap(Generic[KT, VT]):
    def __init__(self, number_of_buckets=7, load_factor=0.75, custom_hash_function: Optional[Callable[[KT], int]]=None):
        self.number_of_buckets = number_of_buckets
        self.load_factor = load_factor
        self.hash_function = custom_hash_function or self._default_hash_function
        self.buckets = [LinkedList() for _ in range(self.number_of_buckets)]
        self.size = 0

    def _default_hash_function(self, key: KT) -> int:
        try:
            key_bytes = pickle.dumps(key)
        except Exception:
            key_bytes = repr(key).encode()
        return int(hashlib.md5(key_bytes).hexdigest(), 16)

    def __setitem__(self, key: KT, value: VT) -> None:
        index = self.hash_function(key) % self.number_of_buckets
        bucket = self.buckets[index]
        node = bucket.find(key)
        if node:
            node.value = value
        else:
            bucket.append(key, value)
            self.size += 1
            if self.size / self.number_of_buckets > self.load_factor:
                self._resize()

    def __getitem__(self, key: KT) -> VT:
        index = self.hash_function(key) % self.number_of_buckets
        bucket = self.buckets[index]
        node = bucket.find(key)
        if node:
            return node.value
        raise KeyError(f"Key {key} not found")

    def __delitem__(self, key: KT) -> None:
        index = self.hash_function(key) % self.number_of_buckets
        if self.buckets[index].remove(key):
            self.size -= 1
        else:
            raise KeyError(f"Key {key} not found")

    def __contains__(self, key: KT) -> bool:
        index = self.hash_function(key) % self.number_of_buckets
        return self.buckets[index].find(key) is not None

    def __len__(self) -> int:
        return self.size

    def __iter__(self) -> Iterator[KT]:
        for bucket in self.buckets:
            for node in bucket:
                yield node.key

    def items(self) -> Iterator[Tuple[KT, VT]]:
        for bucket in self.buckets:
            for node in bucket:
                yield (node.key, node.value)

    def keys(self) -> Iterator[KT]:
        for key, _ in self.items():
            yield key

    def values(self) -> Iterator[VT]:
        for _, value in self.items():
            yield value

    def __eq__(self, other: object) -> bool:
        if isinstance(other, HashMap):
            return set(self.items()) == set(other.items())
        return False

    def __str__(self) -> str:
        return "{" + ", ".join(f"{key}: {value}" for key, value in self.items()) + "}"

    def __repr__(self) -> str:
        return f"HashMap({str(self)})"

    def _resize(self) -> None:
        old_items = list(self.items())
        self.number_of_buckets *= 2
        self.buckets = [LinkedList() for _ in range(self.number_of_buckets)]
        self.size = 0
        for key, value in old_items:
            self[key] = value

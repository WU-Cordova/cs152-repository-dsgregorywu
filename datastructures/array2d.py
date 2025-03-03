from __future__ import annotations
from typing import Iterator, Sequence, TypeVar
from datastructures.iarray import IArray
from datastructures.array import Array
from datastructures.iarray2d import IArray2D

T = TypeVar("T")

class Array2D(IArray2D[T]):

    class Row(IArray2D.IRow[T]):
        def __init__(self, row_index: int, array: IArray, num_columns: int, data_type: type) -> None:
            if not isinstance(data_type, type): raise ValueError("The provided data type is not a valid type.")
            self.row_index = row_index
            self.array = array
            self.num_columns = num_columns
            self.data_type = data_type

        def __getitem__(self, column_index: int) -> T: 
            if not (0 <= column_index < self.num_columns):
                raise IndexError("Column index out of range.")
            index = self.map_index(self.row_index, column_index)
            return self.array[index]
                
        def __setitem__(self, column_index: int, value: T) -> None:
            index = self.map_index(self.row_index, column_index)
            self.array[index] = value

        def __iter__(self) -> Iterator[T]:
            return (self[col_index] for col_index in range(self.num_columns))

        def __len__(self) -> int:
            return self.num_columns
        
        def map_index(self, row_index: int, column_index: int) -> int:
            return row_index * self.num_columns + column_index
        
        def __reversed__(self) -> Iterator[T]:
            return (self[col_index] for col_index in reversed(range(self.num_columns)))

        def __str__(self) -> str:
            return f"[{', '.join(map(str, (self[col_index] for col_index in range(self.num_columns))))}]"
        
        def __repr__(self) -> str:
            return f"Row {self.row_index}: {self.__str__()}"

    def __init__(self, starting_sequence: Sequence[Sequence[T]] = [[]], data_type=object) -> None:
        if not isinstance(starting_sequence, Sequence) or isinstance(starting_sequence, (str, bytes)):
            raise ValueError("The provided data container must be a sequence of sequences.")
        if any(not isinstance(row, Sequence) or isinstance(row, (str, bytes)) for row in starting_sequence):
            raise ValueError("Each row must be a sequence (e.g., list or tuple), not a string or other non-sequence type.")
        self.row_len = len(starting_sequence)
        self.column_len = len(starting_sequence[0]) if self.row_len > 0 else 0
        self.data_type = data_type
        if any(len(row) != self.column_len for row in starting_sequence):
            raise ValueError("All rows must have the same length")
        flattened = [item for row in starting_sequence for item in row]
        if any(not isinstance(item, data_type) for item in flattened):
            raise ValueError("All items must be of the same type")
        self.array2d = Array(flattened, data_type=data_type)

    @staticmethod
    def empty(rows: int = 0, cols: int = 0, data_type: type = object) -> Array2D:
        starting_sequence = [[data_type() for _ in range(cols)] for _ in range(rows)]
        return Array2D(starting_sequence=starting_sequence, data_type=data_type)
    
    def __getitem__(self, row_index: int) -> Array2D.Row[T]: 
        if not (0 <= row_index < self.row_len):
            raise IndexError("Row index out of range.")
        return Array2D.Row(row_index, self.array2d, self.column_len, self.data_type)

    def __iter__(self) -> Iterator[Array2D.Row[T]]:
        return (self[row_index] for row_index in range(self.row_len))
    
    def __reversed__(self) -> Iterator[Array2D.Row[T]]:
        return (self[row_index] for row_index in reversed(range(self.row_len)))
    
    def __len__(self) -> int: 
        return self.row_len
    
    def __str__(self) -> str:
        return f"[{', '.join(str(self[row_index]) for row_index in range(self.row_len))}]"
    
    def __repr__(self) -> str:
        return f"Array2D {self.row_len} Rows x {self.column_len} Columns, items: {self}"

if __name__ == "__main__":
    myarray = Array2D([[1, 2], [3, 4]])
    print(myarray[1][1])

from __future__ import annotations
from typing import Iterator, Sequence, TypeVar
from datastructures.iarray import IArray
from datastructures.array import Array
from datastructures.iarray2d import IArray2D

T = TypeVar("T")

class Array2D(IArray2D[T]):

    class Row(IArray2D.IRow[T]):
        def __init__(self, row_index: int, array: IArray, num_columns: int, data_type: int) -> None:
            self.row_index = row_index
            self.array = array
            self.num_columns = num_columns
            self.row_data = Array([0] * num_columns)  
            self.data_type = data_type
        
        def __getitem__(self, column_index: int) -> T: 
            index = self.map_index(self.row_index, column_index)
            return self.array[index]
                
        def __setitem__(self, column_index: int, value: T) -> None:
            index = self.map_index(self.row_index, column_index)
            self.array[index] = value

        def __iter__(self) -> Iterator[T]:
            for column_index in range(self.num_columns):
                yield self[column_index]

        def __len__(self) -> int:
            return self.num_columns
        
        def map_index(self, row_index: int, column_index: int) -> int:
            raise NotImplementedError()

        def __str__(self) -> str:
            return f"[{', '.join(map(str, self._row_data))}]"
        
        def __repr__(self) -> str:
            return f"Row {self.row_index}: {self.__str__()}"

    def __init__(self, starting_sequence: Sequence[Sequence[T]] = [[]], data_type=object) -> None:
        self.num_rows = len(starting_sequence)
        self.num_columns = len(starting_sequence[0]) if self.num_rows > 0 else 0
        self.data_type = data_type
        self._rows = [Array2D.Row(i, self.num_columns) for i in range(self.num_rows)]
        for i, row in enumerate(starting_sequence):
            for j, value in enumerate(row):
                self._rows[i][j] = value  
    
    @staticmethod
    def empty(rows: int = 0, cols: int = 0, data_type: type = object) -> Array2D:
        return Array2D([[0] * cols for _ in range(rows)], data_type)
    
    def __getitem__(self, row_index: int) -> Array2D.IRow[T]: 
        return self._rows[row_index]

    def __iter__(self) -> Iterator[Sequence[T]]:
        return iter(self._rows)
    
    def __len__(self): 
        return self.num_rows
    
    def __str__(self) -> str:
        return f"[{', '.join(str(row) for row in self._rows)}]"
    
    def __repr__(self) -> str:
        return f"Array2D {self.num_rows} Rows x {self.num_columns} Columns, items: {self}"

if __name__ == "__main__":
    myarray = Array2D
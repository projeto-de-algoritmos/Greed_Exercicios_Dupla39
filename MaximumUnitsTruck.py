from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Ordenar as caixas em ordem decrescente com base no número de unidades por caixa
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        total_units = 0

        for boxes, units in boxTypes:
            if truckSize >= boxes:
                # Se o número de caixas do tipo atual for menor ou igual ao espaço disponível no caminhão,
                # adicione todas as caixas desse tipo e suas unidades
                total_units += boxes * units
                truckSize -= boxes
            else:
                # Caso contrário, adicione apenas a quantidade de caixas possível, de acordo com o espaço disponível
                total_units += truckSize * units
                break

        return total_units
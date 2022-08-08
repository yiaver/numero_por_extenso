#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Numeros:
    def __init__(self) -> None:
        self.__lista_numeros_0_a_9 = [x for x in range(10)]
        self.__lista_de_numero_por_extenso_0_a_9 = ["Zero","Um","Dois","Tres","Quatro","Cinco","Seis","Sete","Oito","Nove"]
        self.__lista_dos_10_e_algo = ["","Onze","Doze","Treze","Quatorze","Quinze","Dezeseis","Dezesete","Dezoito","Dezenove"]
        self.__lista_de_numero_por_extenso_Dezenas = [" ","Dez","Vinte","Trinta","Quarenta","Cinquenta","Sessenta","Setenta","Oitenta","Noventa"]
        self.__lista_de_numero_por_extenso_Centenas = ["","Cem","Dozentos","Trezentos","Quatrocentos","Quinhentos","Seicentos","Setecentos","Oitocentos","Novecentos","Cento"]
    
    @property
    def lista_numeros_0_a_9(self):
        return self.__lista_numeros_0_a_9
    @property
    def lista_de_numero_por_extenso_0_a_9(self):
        return self.__lista_de_numero_por_extenso_0_a_9
    @property
    def lista_dos_10_e_algo(self):
        return self.__lista_dos_10_e_algo
    @property
    def lista_de_numero_por_extenso_Dezenas(self):
        return self.__lista_de_numero_por_extenso_Dezenas
    @property
    def lista_de_numero_por_extenso_Centenas(self):
        return self.__lista_de_numero_por_extenso_Centenas

    def main(self,emtrada_numero):

        if len(str(emtrada_numero)) == 1:
            contador1 = 0
            for n in self.lista_numeros_0_a_9:
                if n == emtrada_numero:
                    return self.lista_de_numero_por_extenso_0_a_9[contador1]
                contador1 += 1
        ###
        elif len(str(emtrada_numero)) == 2:
            numero_str = str(emtrada_numero)
            temp_lista = []
            for n2 in self.lista_numeros_0_a_9[1:]:
                if f"{n2}" == numero_str[0]:
                    temp_var = self.lista_de_numero_por_extenso_Dezenas[n2]
                    temp_lista.append(temp_var)
                    temp_var = ""
                    break

            for nn2 in self.lista_numeros_0_a_9[1:]:
                if numero_str[1] == "0":
                    break
                if numero_str[0] == "1":
                    if f"{nn2}" == numero_str[1]:
                        temp_lista.clear()
                    if f"{nn2}" == numero_str[1]:
                        temp_var1 = self.lista_dos_10_e_algo[nn2]
                        temp_lista.append(temp_var1)
                        temp_var1 = ""
                        break
                if f"{nn2}" == numero_str[1]:
                    temp_var2 = f"e {self.lista_de_numero_por_extenso_0_a_9[nn2]}"
                    temp_lista.append(temp_var2)
                    temp_var = ""
                    break
            output_string = "".join(f"{temp_lista}").replace(","," ").replace("'","").replace("[","").replace("]","")
            temp_lista.clear()
            return output_string
            
        ###
        elif len(str(emtrada_numero)) == 3:
            numero_str = str(emtrada_numero)
            temp_lista = []
            for n2 in self.lista_numeros_0_a_9[1:]:
                if f"{n2}" == numero_str[0]:
                    temp_var = self.lista_de_numero_por_extenso_Centenas[n2]
                    temp_lista.append(temp_var)
                    temp_var = ""
                    break
            for nn2 in self.lista_numeros_0_a_9:
                numero_final = int(numero_str[-1])
                if numero_str[1] == "0" and numero_str[2] == "0":
                    break

                if numero_str[0] == "1":
                    temp_lista.clear()
                    temp_var1 = f"{self.lista_de_numero_por_extenso_Centenas[-1]} e"
                    temp_lista.append(temp_var1)
                    if numero_str[1] == "1":
                        temp_var2 = self.lista_dos_10_e_algo[numero_final]
                        temp_lista.append(temp_var2)
                        break
                    elif numero_str[1] != "1":
                        numero_meio = int(numero_str[1])
                        temp_var3 = f"{self.lista_de_numero_por_extenso_Dezenas[numero_meio]} e"
                        temp_lista.append(temp_var3)
                        temp_var4 = self.lista_de_numero_por_extenso_0_a_9[numero_final]
                        temp_lista.append(temp_var4)
                        break
                if numero_str[0] != "1":
                    temp_lista.append("e")
                    if numero_str[1] == "1":
                        temp_var2 = self.lista_dos_10_e_algo[numero_final]
                        temp_lista.append(temp_var2)
                        break
                    elif numero_str[1] != "1":
                        numero_meio = int(numero_str[1])
                        temp_var3 = f"{self.lista_de_numero_por_extenso_Dezenas[numero_meio]} e"
                        temp_lista.append(temp_var3)
                        temp_var4 = self.lista_de_numero_por_extenso_0_a_9[numero_final]
                        temp_lista.append(temp_var4)
                        break
        
            output_string = "".join(f"{temp_lista}").replace(","," ").replace("'","").replace("[","").replace("]","")
            if output_string.endswith("e  Zero"):
                output_string = output_string.replace("e  Zero","")
            temp_lista.clear()
            return output_string



if __name__ == "__main__":
    emtrada = int(input(f"Digite um numero: "))
    pex = Numeros()
    print(pex.main(emtrada_numero=emtrada))
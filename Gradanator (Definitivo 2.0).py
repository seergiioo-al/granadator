
def homework_score(): # creamos una funcion en la que recogemos la nota de los diferentes trabajos y creamos una variable que ya tenga calculado el peso del trabajo
    while True:
        try:
            homework_1 = int(input("Introduce la puntuación obtenida H1, nota máxima 15: "))
            while homework_1 >15:
                print ("El valor no puede ser superior a 15")
                homework_1 = int(input("Introduce la puntuación obtenida H1: "))
            
            homework_2 = int (input("Introduce la puntuación obtenida H2, nota máxima 20: "))
            while homework_2 > 20:
                print ("El valor introducido no puede ser superior a 20")
                homework_2 = int(input("Introduce la puntuación obtenida H2"))
            
            homework_3 = int(input("Introduce la puntuación obtenida H3, nota máxima 25: "))
            while homework_3 > 25:
                print ("El valor introducido no puede ser superior a 25")
                homework_3 = int(input("introduce la puntuación obtenida H3"))
            peso_trabajos = float(input("Introduce el peso del trabajo: "))

            homework = (((homework_1 + homework_2 + homework_3) /60) * peso_trabajos)
            return homework
        
        except ValueError:
            print ("Introduce valores validos")
            return homework_score()

def grade(final_homework):
    try:    
        exam_1 = float(input("Introduce la nota de tu primer examen: "))
        if exam_1 > 100:
            print("El valor introducido no puede ser mayor de 100")
            exam_1 = float(input("Introduce la nota de tu primer examen: "))
        
        peso_exam_1 = float(input("Introduce el peso del primer examen: "))
        examen_1_NotaFinal = ((exam_1 /100) * peso_exam_1)
        print(f"Nota final examen 1: {examen_1_NotaFinal}")

        exam_2 = float(input("Introduce la nota obtenida en tu segundo examen: "))
        if exam_2 > 100:
            print ("El valor introducido no puede ser mayor a 100")
            exam_2 = float(input("Introduce la nota obtenida en tu segundo examen: "))

        peso_exam_2 = float(input("introduce el peso del segundo examen: "))
        examen_2_NotaFinal = ((exam_2/100)* peso_exam_2)
        print(f"Nota final examen 2: {examen_2_NotaFinal}")

        exam_3 = float(input("Introduce la nota obtenida en tu tercer examen: "))
        if exam_3 > 100:
            print("El valor introducido no puede ser mayor de 100")
            exam_3 = float(input("Introduce la nota obtenida en tu tercer examen: "))

        peso_exam_3 = float(input("Introduce el peso del tercer examen: "))
        examen_3_NotaFinal = ((exam_3 / 100) *peso_exam_3)
        print(f"Nota final examen final: {examen_3_NotaFinal}")

        final_grade = examen_1_NotaFinal + examen_2_NotaFinal + examen_3_NotaFinal + final_homework
        return final_grade
    except ValueError:
        print ("Introduce valores validos")
        return grade(final_homework)

def nota_letra (result):
    if result > 90:
        return "A, Muy bien máquina"
    elif 80< result <89.99:
        return "B, No esta mal pero es mejorable"
    elif 70 < result < 79.99:
        return "C, vas justito"
    elif 60 < result <69.99:
        return "D, Casi lo consigues pero vuelve a intentarlo"
    elif result <60:
        return "F, has suspendido parguela"
    
    letra = nota_letra(result)

    print (f"Tu nota final es: {round(result,2)}% equivalente a la letra: {letra}")

def main():
    final_homework = homework_score()

    result = grade(final_homework)

    letra = nota_letra(result)

    print(f"Tu nota final es: {round(result, 2)}% equivalente a la letra: {letra}")

main()

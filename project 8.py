def main():
    temp = input("Please enter the average daily temperatures with a space between each: ")
    temp = temp.split(" ")

    cool=0
    heat=0

    for i in temp:
        if float(i)>80 or float(i)<60:
            if float(i)>80:
                cool+=float(i)-80
            else:
                heat+=60-float(i)
    print("The cooling degree days are:", cool)
    print("The heating degree days are:", heat)

main()

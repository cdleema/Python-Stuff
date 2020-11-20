
def main():
    f = open("temp.txt", "w")
    link = '<a href="https://www.volarenovels.com/novel/destroyer-of-ice-and-fire/dif-chapter-'

    for x in range(702):
        f.write(link + str(x) + '">Chapter ' + str(x) + '</a>\n')

    f.close()

##    for x in range(10):
##        print(link + str(x) + '>Chapter ' + str(x) + '</a>\n')
if __name__ == "__main__":
    main()

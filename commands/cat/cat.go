package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func readfile(file string) string {
	dat, err := ioutil.ReadFile(file)
	check(err)
	return string(dat)
}

func main() {
	files := os.Args[1:]

	var cat string = ""

	if len(files) == 0 {
		fmt.Println("You must enter a file.")
		os.Exit(1)
	}

	for i := 0; i < len(files); i++ {
		cat = cat + readfile(files[i])
	}

	fmt.Print(cat)

}

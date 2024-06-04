package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func main() {
	var N int
	var s string
	scanner := bufio.NewScanner(os.Stdin)
	if scanner.Scan() {
		N, _ = strconv.Atoi(scanner.Text())
	}

	if scanner.Scan() {
		s = scanner.Text()
	}

	fmt.Scanf("%s", &s)
	fracS := strings.Split(s, " ")
	var frac = make([]int, N)
	for i, e := range fracS {
		s, err := strconv.Atoi(e)
		if err != nil {
			panic(err)
		}
		frac[i] = s
	}
	slices.Sort(frac)
	if N%2 == 0 {
		fmt.Print(frac[0] * frac[N-1])
	} else {
		mid := len(frac) / 2
		fmt.Print(frac[mid] * frac[mid])
	}
}

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func partOne(arr []string) int {
	count := 0

	for _, line := range arr {
		pairs := strings.Split(line, ",")
		p1 := strings.Split(pairs[0], "-")
		p2 := strings.Split(pairs[1], "-")
		l1, _ := strconv.Atoi(p1[0])
		r1, _ := strconv.Atoi(p1[1])
		l2, _ := strconv.Atoi(p2[0])
		r2, _ := strconv.Atoi(p2[1])

		if l1 <= l2 && r2 <= r1 || l2 <= l1 && r1 <= r2 {
			count++
		}
	}

	return count
}

func partTwo(arr []string) int {
	count := 0

	for _, line := range arr {
		pairs := strings.Split(line, ",")
		p1 := strings.Split(pairs[0], "-")
		p2 := strings.Split(pairs[1], "-")
		l1, _ := strconv.Atoi(p1[0])
		r1, _ := strconv.Atoi(p1[1])
		l2, _ := strconv.Atoi(p2[0])
		r2, _ := strconv.Atoi(p2[1])

		if !(r1 < l2 || r2 < l1) {
			count++
		}
	}

	return count
}

func main() {
	input, err := readLines("input.txt")
	if err != nil {
		panic(err)
	}

	fmt.Printf("Part 1: %d\n", partOne(input))
	fmt.Printf("Part 2: %d\n", partTwo(input))
}

func readLines(path string) ([]string, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines, scanner.Err()
}

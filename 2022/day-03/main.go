package main

import (
	"bufio"
	"fmt"
	"os"
	"unicode"
)

func priority(r rune) int {
	if unicode.IsLower(r) {
		return int(r) - int('a') + 1
	}

	return int(r) - int('A') + 27
}

func partOne(arr []string) int {
	sum := 0

	for _, rucksack := range arr {
		com1 := rucksack[:len(rucksack)/2]
		com2 := rucksack[len(rucksack)/2:]
		set := make(map[rune]struct{}, len(com1))
		var sharedChar rune

		for _, r := range com1 {
			set[r] = struct{}{}
		}

		for _, r := range com2 {
			if _, ok := set[r]; ok {
				sharedChar = r
				break
			}
		}

		sum += priority(sharedChar)
	}

	return sum
}

func partTwo(arr []string) int {
	sum := 0

	nGroups := len(arr) / 3
	for i := 0; i < nGroups; i++ {
		startIdx := i * 3
		var seen [54]bool

		for _, r := range arr[startIdx] {
			seen[priority(r)-1] = true
		}

		for j := 1; j < 3; j++ {
			var tmpSeen [54]bool
			for _, r := range arr[startIdx+j] {
				idx := priority(r) - 1
				if seen[idx] {
					tmpSeen[idx] = true
				}
			}
			seen = tmpSeen
		}

		for j := 0; j < len(seen); j++ {
			if seen[j] {
				sum += j + 1
				break
			}
		}
	}

	return sum
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

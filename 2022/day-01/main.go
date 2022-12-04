package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func partOne(arr []string) int {
	if arr[len(arr)-1] != "" {
		arr = append(arr, "")
	}

	max := 0
	acc := 0

	for _, valueStr := range arr {
		if valueStr == "" {
			if acc > max {
				max = acc
			}

			acc = 0
		}

		val, _ := strconv.Atoi(valueStr)
		acc += val
	}

	return max
}

func partTwo(arr []string) int {
	if arr[len(arr)-1] != "" {
		arr = append(arr, "")
	}

	var top3 [3]int
	acc := 0

	for _, valueStr := range arr {
		if valueStr == "" {
			if acc >= top3[0] {
				top3[2] = top3[1]
				top3[1] = top3[0]
				top3[0] = acc
			} else if acc >= top3[1] {
				top3[2] = top3[1]
				top3[1] = acc
			} else if acc > top3[2] {
				top3[2] = acc
			}

			acc = 0
		}

		val, _ := strconv.Atoi(valueStr)
		acc += val
	}

	return top3[0] + top3[1] + top3[2]
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

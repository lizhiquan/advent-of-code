package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func PartOne(arr []string) int {
	hPos := 0
	depth := 0

	for _, item := range arr {
		components := strings.Split(item, " ")
		command := components[0]
		value, err := strconv.Atoi(components[1])
		if err != nil {
			return -1
		}

		switch command {
		case "forward":
			hPos += value
		case "down":
			depth += value
		case "up":
			depth -= value
		}
	}

	return hPos * depth
}

func PartTwo(arr []string) int {
	hPos := 0
	depth := 0
	aim := 0

	for _, item := range arr {
		components := strings.Split(item, " ")
		command := components[0]
		value, err := strconv.Atoi(components[1])
		if err != nil {
			return -1
		}

		switch command {
		case "forward":
			hPos += value
			depth += aim * value
		case "down":
			aim += value
		case "up":
			aim -= value
		}
	}

	return hPos * depth
}

func main() {
	input, err := readLines("input.txt")
	if err != nil {
		fmt.Println(err)
		os.Exit(2)
	}

	fmt.Printf("Part 1: %d\n", PartOne(input))
	fmt.Printf("Part 2: %d\n", PartTwo(input))
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

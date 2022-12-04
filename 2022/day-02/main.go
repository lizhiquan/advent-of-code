package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const (
	opponentRock     = "A"
	opponentPaper    = "B"
	opponentScissors = "C"

	myRock     = "X"
	myPaper    = "Y"
	myScissors = "Z"

	roundLose = "X"
	roundDraw = "Y"
	roundWin  = "Z"
)

var shapeScore = map[string]int{
	myRock:     1,
	myPaper:    2,
	myScissors: 3,
}

var roundScore = map[string]int{
	roundLose: 0,
	roundDraw: 3,
	roundWin:  6,
}

func partOne(arr []string) int {
	score := 0

	for _, line := range arr {
		choices := strings.Split(line, " ")
		opponentChoice := choices[0]
		myChoice := choices[1]
		var roundResult string

		switch opponentChoice {
		case opponentRock:
			switch myChoice {
			case myRock:
				roundResult = roundDraw
			case myPaper:
				roundResult = roundWin
			case myScissors:
				roundResult = roundLose
			}

		case opponentPaper:
			switch myChoice {
			case myRock:
				roundResult = roundLose
			case myPaper:
				roundResult = roundDraw
			case myScissors:
				roundResult = roundWin
			}

		case opponentScissors:
			switch myChoice {
			case myRock:
				roundResult = roundWin
			case myPaper:
				roundResult = roundLose
			case myScissors:
				roundResult = roundDraw
			}
		}

		score += roundScore[roundResult] + shapeScore[myChoice]
	}

	return score
}

func partTwo(arr []string) int {
	score := 0

	for _, line := range arr {
		choices := strings.Split(line, " ")
		opponentChoice := choices[0]
		roundResult := choices[1]
		var myChoice string

		switch opponentChoice {
		case opponentRock:
			switch roundResult {
			case roundLose:
				myChoice = myScissors
			case roundDraw:
				myChoice = myRock
			case roundWin:
				myChoice = myPaper
			}

		case opponentPaper:
			switch roundResult {
			case roundLose:
				myChoice = myRock
			case roundDraw:
				myChoice = myPaper
			case roundWin:
				myChoice = myScissors
			}

		case opponentScissors:
			switch roundResult {
			case roundLose:
				myChoice = myPaper
			case roundDraw:
				myChoice = myScissors
			case roundWin:
				myChoice = myRock
			}
		}

		score += roundScore[roundResult] + shapeScore[myChoice]
	}

	return score
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

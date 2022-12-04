package main

import "testing"

func TestPartOne(t *testing.T) {
	input, err := readLines("input_test.txt")
	if err != nil {
		panic(err)
	}

	got := partOne(input)
	want := 2
	if got != want {
		t.Errorf("got %v, wanted %v", got, want)
	}
}

func TestPartTwo(t *testing.T) {
	input, err := readLines("input_test.txt")
	if err != nil {
		panic(err)
	}

	got := partTwo(input)
	want := 4
	if got != want {
		t.Errorf("got %v, wanted %v", got, want)
	}
}

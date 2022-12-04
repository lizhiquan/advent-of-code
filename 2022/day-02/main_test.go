package main

import "testing"

func TestPartOne(t *testing.T) {
	input, err := readLines("input_test.txt")
	if err != nil {
		panic(err)
	}

	got := partOne(input)
	want := 15
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
	want := 12
	if got != want {
		t.Errorf("got %v, wanted %v", got, want)
	}
}

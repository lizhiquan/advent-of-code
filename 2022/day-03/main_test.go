package main

import "testing"

func TestPartOne(t *testing.T) {
	input, err := readLines("input_test.txt")
	if err != nil {
		panic(err)
	}

	got := partOne(input)
	want := 157
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
	want := 70
	if got != want {
		t.Errorf("got %v, wanted %v", got, want)
	}
}

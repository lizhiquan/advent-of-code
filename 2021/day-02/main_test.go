package main

import "testing"

func TestPartOne(t *testing.T) {
	input := []string{
		"forward 5",
		"down 5",
		"forward 8",
		"up 3",
		"down 8",
		"forward 2",
	}
	got := PartOne(input)
	want := 150
	if got != want {
		t.Errorf("got %q, wanted %q", got, want)
	}
}

func TestPartTwo(t *testing.T) {
	input := []string{
		"forward 5",
		"down 5",
		"forward 8",
		"up 3",
		"down 8",
		"forward 2",
	}
	got := PartTwo(input)
	want := 900
	if got != want {
		t.Errorf("got %q, wanted %q", got, want)
	}
}

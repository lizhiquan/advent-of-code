use std::collections::HashMap;
use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    println!("Part 1: {}", part1());
    println!("Part 2: {}", part2());
}

fn part1() -> u32 {
    let file = File::open("input.txt").unwrap();
    let reader = BufReader::new(file);

    reader.lines()
        .filter_map(Result::ok)
        .map(|line| {
            let first = line.chars()
                .find(|c| c.is_digit(10)).unwrap()
                .to_digit(10).unwrap();

            let second = line.chars()
                .rfind(|c| c.is_digit(10)).unwrap()
                .to_digit(10).unwrap();

            first * 10 + second
        })
        .sum()
}


fn part2() -> u32 {
    let file = File::open("input.txt").unwrap();
    let reader = BufReader::new(file);
    let number_map = HashMap::from([
        ("one", 1),
        ("two", 2),
        ("three", 3),
        ("four", 4),
        ("five", 5),
        ("six", 6),
        ("seven", 7),
        ("eight", 8),
        ("nine", 9),
        ("1", 1),
        ("2", 2),
        ("3", 3),
        ("4", 4),
        ("5", 5),
        ("6", 6),
        ("7", 7),
        ("8", 8),
        ("9", 9),
    ]);

    reader.lines()
        .filter_map(Result::ok)
        .map(|line| {
            let first = number_map.keys().into_iter()
                .filter_map(|num_str| {
                    line.find(num_str).map(|index| (num_str, index))
                })
                .min_by_key(|(_num_str, index)| index.clone())
                .unwrap().0;

            let second = number_map.keys().into_iter()
                .filter_map(|num_str| {
                    line.rfind(num_str).map(|index| (num_str, index))
                })
                .max_by_key(|(_num_str, index)| index.clone())
                .unwrap().0;

            number_map[first] * 10 + number_map[second]
        })
        .sum()
}

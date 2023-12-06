use std::collections::HashSet;
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
            let parts: Vec<&str> = line.split(": ")
                .nth(1).unwrap()
                .split(" | ").collect();
            let winning_numbers: HashSet<&str> = HashSet::from_iter(parts[0].split_whitespace());
            let having_numbers: HashSet<&str> = HashSet::from_iter(parts[1].split_whitespace());
            let matches = having_numbers.intersection(&winning_numbers).count();
            if matches == 0 {
                return 0;
            }
            2_u32.pow((matches - 1) as u32)
        })
        .sum()
}

fn part2() -> u32 {
    let file = File::open("input.txt").unwrap();
    let reader = BufReader::new(file);
    let matches: Vec<usize> = reader.lines()
        .filter_map(Result::ok)
        .map(|line| {
            let parts: Vec<&str> = line.split(": ")
                .nth(1).unwrap()
                .split(" | ").collect();
            let winning_numbers: HashSet<&str> = HashSet::from_iter(parts[0].split_whitespace());
            let having_numbers: HashSet<&str> = HashSet::from_iter(parts[1].split_whitespace());
            having_numbers.intersection(&winning_numbers).count()
        })
        .collect();

    let mut count = vec![1; matches.len()];
    for i in 0..matches.len() {
        for j in 0..matches[i] {
            count[i + 1 + j] += count[i];
        }
    }
    count.iter().sum()
}

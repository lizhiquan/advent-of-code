use std::collections::HashMap;
use std::fs::File;
use std::io::{BufRead, BufReader};
use regex::Regex;

fn main() {
    println!("Part 1: {}", part1());
    // println!("Part 2: {}", part2());
}

fn part1() -> u32 {
    let file = File::open("input.txt").unwrap();
    let mut lines = BufReader::new(file).lines();
    let instructions = lines.next().unwrap().unwrap();
    lines.next();
    let re = Regex::new(r"(\w+) = \((\w+), (\w+)\)").unwrap();
    let map = lines
        .filter_map(Result::ok)
        .fold(HashMap::new(), |mut acc, line| {
            let captures = re.captures(line.as_str()).unwrap();
            let node = captures.get(1).unwrap().as_str();
            let left = captures.get(2).unwrap().as_str();
            let right = captures.get(3).unwrap().as_str();
            acc.insert(node.to_string(), (left.to_string(), right.to_string()));
            acc
        });

    let mut count = 0;
    let mut current = "AAA";
    for instruction in instructions.chars().cycle() {
        let (left, right) = map.get(current).unwrap();
        if instruction == 'L' {
            current = left;
        } else if instruction == 'R' {
            current = right;
        }
        count += 1;
        if current == "ZZZ" {
            break;
        }
    }
    count
}

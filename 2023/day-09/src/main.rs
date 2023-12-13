use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    println!("Part 1: {}", part1());
    println!("Part 2: {}", part2());
}

fn part1() -> i32 {
    let file = File::open("input.txt").unwrap();
    BufReader::new(file)
        .lines()
        .filter_map(Result::ok)
        .map(|line| {
            let mut nums: Vec<i32> = line.split_whitespace()
                .map(|x| x.parse::<i32>().unwrap())
                .collect();

            let mut len = nums.len();
            while len > 1 {
                let mut should_break = true;
                for i in 0..len - 1 {
                    nums[i] = nums[i + 1] - nums[i];
                    if nums[i] != 0 {
                        should_break = false;
                    }
                }
                len -= 1;
                if should_break {
                    break;
                }
            }

            nums[len..].iter().sum::<i32>()
        })
        .sum()
}

fn part2() -> i32 {
    let file = File::open("input.txt").unwrap();
    BufReader::new(file)
        .lines()
        .filter_map(Result::ok)
        .map(|line| {
            let mut nums: Vec<i32> = line.split_whitespace()
                .map(|x| x.parse::<i32>().unwrap())
                .collect();

            let mut start = 1;
            while start < nums.len() {
                let mut should_break = true;
                for i in (start..nums.len()).rev() {
                    nums[i] = nums[i] - nums[i - 1];
                    if nums[i] != 0 {
                        should_break = false;
                    }
                }
                start += 1;
                if should_break {
                    break;
                }
            }

            for i in (1..start).rev() {
                nums[i - 1] = nums[i - 1] - nums[i];
            }
            nums[0]
        })
        .sum()
}

use std::collections::{HashSet, VecDeque};
use std::fs::read_to_string;

fn main() {
    println!("Part 1: {}", part1("input.txt"));
}

fn can_go_up(from: &char, to: &char) -> bool {
    (from == &'S' || from == &'|' || from == &'L' || from == &'J') &&
        (to == &'S' || to == &'|' || to == &'7' || to == &'F')
}

fn can_go_left(from: &char, to: &char) -> bool {
    (from == &'S' || from == &'-' || from == &'7' || from == &'J') &&
        (to == &'S' || to == &'-' || to == &'F' || to == &'L')
}

fn part1(input: &str) -> u32 {
    let map: Vec<Vec<char>> = read_to_string(input).unwrap()
        .lines()
        .map(|l| l.chars().collect())
        .collect();

    let mut start = (0, 0);
    for (r, row) in map.iter().enumerate() {
        for (c, col) in row.iter().enumerate() {
            if *col == 'S' {
                start = (r, c);
            }
        }
    }

    let mut visited = HashSet::new();
    let mut queue = VecDeque::new();
    queue.push_back((start, 0));

    enum Direction {
        Up,
        Down,
        Left,
        Right,
    }

    impl Direction {
        fn delta(&self) -> (i32, i32) {
            match self {
                Direction::Up => (-1, 0),
                Direction::Down => (1, 0),
                Direction::Left => (0, -1),
                Direction::Right => (0, 1),
            }
        }
    }

    while let Some(((r, c), dist)) = queue.pop_front() {
        visited.insert((r, c));

        let mut visited_count = 0;
        for direction in vec![Direction::Up, Direction::Down, Direction::Left, Direction::Right] {
            let (dr, dc) = direction.delta();
            let (nr, nc) = (r as i32 + dr, c as i32 + dc);
            if nr >= 0 && nr < map.len() as i32 && nc >= 0 && nc < map[0].len() as i32 {
                let nr = nr as usize;
                let nc = nc as usize;
                let current = &map[r][c];
                let next = &map[nr][nc];

                match direction {
                    Direction::Up => {
                        if !can_go_up(current, next) {
                            continue;
                        }
                    }
                    Direction::Down => {
                        if !can_go_up(next, current) {
                            continue;
                        }
                    }
                    Direction::Left => {
                        if !can_go_left(current, next) {
                            continue;
                        }
                    }
                    Direction::Right => {
                        if !can_go_left(next, current) {
                            continue;
                        }
                    }
                }

                if visited.contains(&(nr, nc)) {
                    visited_count += 1;

                    if visited_count == 2 {
                        // found the loop
                        return dist;
                    }

                    continue;
                }

                queue.push_back(((nr, nc), dist + 1));
            }
        }
    }

    0
}

fn part2(input: &str) -> u32 {
    0
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1() {
        assert_eq!(part1("input_test1.txt"), 4);
        assert_eq!(part1("input_test2.txt"), 8);
    }

    #[test]
    fn test_part2() {
        assert_eq!(part2("input_test2.txt"), 0);
    }
}

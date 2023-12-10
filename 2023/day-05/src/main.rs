use std::fs::read_to_string;

fn main() {
    println!("Part 1: {}", part1());
    // println!("Part 2: {}", part2());
}

fn part1() -> u64 {
    let content = read_to_string("input.txt").unwrap();
    let mut parts = content.split("\n\n");
    let seeds: Vec<u64> = parts
        .next().unwrap()
        .split(": ")
        .nth(1).unwrap()
        .split_whitespace()
        .filter_map(|num| num.parse().ok())
        .collect();
    let maps: Vec<Vec<Vec<u64>>> = parts
        .map(|block|
            block.split("\n")
                .skip(1)
                .map(|line|
                    line.split_whitespace()
                        .filter_map(|num| num.parse().ok())
                        .collect::<Vec<u64>>()
                )
                .collect::<Vec<Vec<u64>>>()
        )
        .collect();

    let positions: Vec<u64> = seeds.iter()
        .map(|x| {
            let mut tmp_x = *x;
            for map_block in &maps {
                for map in map_block {
                    let [s, d, r] = map.as_slice() else { panic!() };
                    if *d <= tmp_x && tmp_x <= d + r {
                        tmp_x = s + tmp_x - d;
                        break;
                    }
                }
            }
            tmp_x
        })
        .collect();

    positions.iter().min().unwrap().clone()
}

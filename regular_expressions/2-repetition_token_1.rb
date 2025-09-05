#!/usr/bin/env ruby

# Check if an argument is provided
if ARGV.length != 1
  puts "Usage: #{$0} <string_to_match>"
  exit 1
end

# Get the input string from command line argument
input_string = ARGV[0]

# Define the regular expression pattern
# TODO: Replace this with the actual pattern based on your requirements
pattern = /YOUR_REGEX_PATTERN_HERE/

# Find all matches
matches = input_string.scan(pattern)

# Output the matches
if matches.empty?
  puts "No matches found"
else
  matches.each do |match|
    puts match
  end
end

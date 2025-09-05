#!/usr/bin/env ruby

# Check if an argument is provided
if ARGV.length != 1
  puts "Usage: #{$0} <string_to_match>"
  exit 1
end

# Get the input string from command line argument
input_string = ARGV[0]

# Define the regular expression pattern
# Matches 'h' followed by 0 or 1 'b', then 'tn'
pattern = /hb?tn/

# Find all matches
matches = input_string.scan(pattern)

# Output the matches
if matches.empty?
  # For the case where no matches are found, just output empty line
  puts ""
else
  matches.each do |match|
    puts match
  end
end

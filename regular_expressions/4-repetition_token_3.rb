#!/usr/bin/env ruby

# Check if an argument is provided
if ARGV.length != 1
  puts "Usage: #{$0} <string_to_match>"
  exit 1
end

# Get the input string from command line argument
input_string = ARGV[0]

# Define the regular expression pattern
# Note: No square brackets allowed in this regex
# Matches 'h' followed by 'b', then one or more 't', then 'n'
pattern = /hbt+n/

# Find all matches
matches = input_string.scan(pattern)

# Output the matches
if matches.empty?
  puts ""
else
  matches.each do |match|
    puts match
  end
end

#!/usr/bin/perl

# This is a copy of playfair.py except written in Perl

# Define Modules
# use strict;
# use warnings;
use POSIX strftime;
use List::Util shuffle;

# Define Global Variables
my $datestring = strftime  "%F",localtime;
my @choices = (A..Z,0..9);

# Create Alphanumeric Random String
my @shuffled_choices = shuffle @choices;

# Format and Write to a file
my $fname = 'output/' . $datestring . '_' . join('',@shuffled_choices[0..5]) . '.md';

open(outfile,'>',$fname);
print outfile '# ' . $datestring . "\n\n";
print outfile "|" . join('|',@shuffled_choices[0..5]) . "|\n";
print outfile "|" . join('|',(':---:') x 6), "|\n";
print outfile "|" . join('|',@shuffled_choices[6..11]) . "|\n";
print outfile "|" . join('|',@shuffled_choices[12..17]) . "|\n";
print outfile "|" . join('|',@shuffled_choices[18..23]) . "|\n";
print outfile "|" . join('|',@shuffled_choices[24..29]) . "|\n";
print outfile "|" . join('|',@shuffled_choices[30..35]) . "|\n";

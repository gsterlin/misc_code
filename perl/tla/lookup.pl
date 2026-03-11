#!/usr/bin/perl
use strict;
use warnings;

for my $first ('a'..'z', 0..9) {
    for my $second ('a'..'z', 0..9) {
        for my $third ('a'..'z', 0..9) {
            print "$first$second$third\n";
            print `nslookup $first$second$third.com`;
        }
    }
}

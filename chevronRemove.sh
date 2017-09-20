#!/bin/sh
# chevronRemove.sh
# see name for details

DELIM="<" # default delimter
stripSpace="true"

# parse arguments
while [ $# -gt 0 ]; do
	case $1 in
		-h)	cat << "EOF"
Usage: chevronRemove.sh

  -d DELIM    Use this as the comment delimiter.
EOF
			exit 1	;;
		-d)	DELIM="$2" # store desired delimiter
	esac
	shift
done

sed -E 's|<[^>]*>||g' # remove chevrons

exit 0;

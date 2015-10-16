# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
MIN=10000000
ARRAY=()
read N
for (( i=0; i<N; i++ )); do
    read Pi
    ARRAY+=($Pi)
done

function mysort { for i in ${ARRAY[@]}; do echo "$i"; done | sort -n; }

ARRAY=( $(mysort) )

OLD=${ARRAY[0]}

for (( i=0; i<N-1; i++ )); do
    TEMP=${ARRAY[i+1]}
    NEW=$(($TEMP - $OLD)) #$((${ARRAY[i+1]} - ${ARRAY[i]}))
    OLD=$TEMP
    if (($NEW < $MIN)); then
        MIN=$NEW
    fi
done

# Write an action using echo
# To debug: echo "Debug messages..." >&2

echo $MIN

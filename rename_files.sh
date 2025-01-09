for file in ./tic-tac-toe/esercizio*; do
    mv "$file" "${file/esercizio_/exercise_}"
done
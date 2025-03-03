#!/bin/bash

# Output file
OUTPUT_FILE="synthetic_patients.csv"

# Default number of synthetic patients
NUM_PATIENTS=100

# Define arrays of possible values
GENDERS=("Male" "Female" "Non-Binary")
CONDITIONS=("Diabetes" "Hypertension" "Asthma" "Arthritis" "Depression" "Obesity" "No Chronic Condition")
PREFERRED_FORMATS=("Articles" "Videos" "Podcasts" "Infographics")

# Help function
show_help() {
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Generate a synthetic patient dataset."
    echo ""
    echo "Options:"
    echo "  -n, --num-patients <number>  Specify the number of patients to generate (default: 100)."
    echo "  -o, --output <filename>      Specify the output CSV file (default: synthetic_patients.csv)."
    echo "  -h, --help                   Show this help message and exit."
    echo ""
    exit 0
}

# Parse command-line arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
    -n | --num-patients)
        NUM_PATIENTS="$2"
        shift
        ;;
    -o | --output)
        OUTPUT_FILE="$2"
        shift
        ;;
    -h | --help) show_help ;;
    *)
        echo "Unknown option: $1"
        show_help
        ;;
    esac
    shift
done

# Write header to CSV
echo "PatientID,Age,Gender,Condition,PreferredFormat" >"$OUTPUT_FILE"

# Generate random patients
for ((i = 1; i <= NUM_PATIENTS; i++)); do
    # Randomly generate values
    AGE=$((RANDOM % 60 + 18)) # Age between 18 and 77
    GENDER=${GENDERS[$RANDOM % ${#GENDERS[@]}]}
    CONDITION=${CONDITIONS[$RANDOM % ${#CONDITIONS[@]}]}
    FORMAT=${PREFERRED_FORMATS[$RANDOM % ${#PREFERRED_FORMATS[@]}]}

    # Write patient data to CSV
    echo "$i,$AGE,$GENDER,$CONDITION,$FORMAT" >>"$OUTPUT_FILE"
done

echo "✅ Synthetic patient data generated: $OUTPUT_FILE"

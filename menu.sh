#!/bin/bash

function clear_screen() {
    if [ "$(uname)" == "Darwin" ]; then
        clear  # macOS
    elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
        clear  # Linux
    elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]; then
        cmd /c "cls"  # Windows NT - 34 bits
    elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW64_NT" ]; then
        cmd /c "cls"  # Windows NT - 65¿4 bits
    fi
}

function menu() {
    echo -e "\nCifrado de texto\n"
    echo "0. Usage"
    echo "1. Caesar Chiper"
    echo "2. Vigenere Chiper"
    echo -e "3. Salir\n"
}


function usage() {
    echo "Usage: $0 [options]"
    echo "Options:"
    echo "  -h, --help      Show this help message and exit"
    echo "  -v, --version   Show program's version number and exit"
    echo "  -c, --caesar    Use Caesar Chiper"
    echo "  -v, --vigenere  Use Vigenere Chiper"
}
function main() {
    menu

    read -p "Seleccione una opción: " option
    clear_screen()

    case $option in
        0)
            usage
            ;;
        1)
            echo "Caesar Chiper"
            ;;
        2)
            echo "Vigenere Chiper"
            ;;
        3)
            echo "Saliendo..."
            exit 0
            ;;
        *)
            echo "Ingresa una opcion valida!"
            ;;
    esac
}

main
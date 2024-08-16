#IMPORTS    
from send_email import send_emails
import os
import sys

def main():
    send_emails()

    #delete key file and handle possible errors
    file_path = 'python/secret.key'
    try:
        os.remove(file_path)
        print('The key file has been deleted successfully.')
    except FileNotFoundError:
        sys.exit(f'{file_path} does not exist')
    except PermissionError:
        sys.exit(f'Permission denied: {file_path} cannot be deleted')
    except Exception as e:
        sys.exit(f'Error: {e}')

if __name__ == "__main__":
    main()




#SPDX-FileCopyrightText: © 2024 Leonardo Giuliani de Santis <leogiulianidesantis@gmail.com>

#SPDX-License-Identifier: BSD-3-Clause


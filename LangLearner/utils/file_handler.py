import csv
import os


class FileHandler:


    @staticmethod
    def read_csv(file_path):

        data = []


        try:

            if not os.path.exists(file_path):

                return data



            with open(
                file_path,
                "r",
                newline="",
                encoding="utf-8"
            ) as file:


                reader = csv.reader(file)


                for row in reader:

                    data.append(row)



        except Exception as e:

            print(
                "File Read Error:",
                e
            )


        return data





    @staticmethod
    def write_csv(file_path, data):


        try:


            with open(
                file_path,
                "w",
                newline="",
                encoding="utf-8"
            ) as file:


                writer = csv.writer(file)

                writer.writerows(data)



        except Exception as e:


            print(
                "File Write Error:",
                e
            )






    @staticmethod
    def append_csv(file_path, row):


        try:


            with open(
                file_path,
                "a",
                newline="",
                encoding="utf-8"
            ) as file:


                writer = csv.writer(file)

                writer.writerow(row)



        except Exception as e:


            print(
                "File Append Error:",
                e
            )





    @staticmethod
    def file_exists(file_path):

        return os.path.exists(file_path)






    @staticmethod
    def create_file(
        file_path,
        headers=None
    ):


        if not os.path.exists(file_path):


            with open(
                file_path,
                "w",
                newline="",
                encoding="utf-8"
            ) as file:


                writer = csv.writer(file)


                if headers:

                    writer.writerow(headers)





    @staticmethod
    def delete_file(file_path):


        if os.path.exists(file_path):

            os.remove(file_path)
# Mathematical-Structures
A collection of databases of mathematical structures that can be organized into posets.

1. **Clone the repositories**
	- First, clone the main database editor repository:
	  ```bash
	  git clone https://github.com/obousquet/math_database
	  ```
	- Then, clone this data repository:
	  ```bash
	  git clone https://github.com/obousquet/Mathematical-Structures
	  ```

2. **Install requirements**
	- In the `math_database` repository, install the required Python packages:
	  ```bash
	  cd math_database
	  pip install -r requirements.txt
	  ```

3. **Run the local editing server**
	- Start the server, pointing it to the data directory of this repository:
	  ```bash
	  python3 server.py --data-dir=<Mathematical-Structures>/data/<directory of interest>
	  ```

4. **Edit the database locally**
	- Open your browser and go to [http://localhost:8080](http://localhost:8080)
	- You can now edit, add, or update entries in the database. All changes will be saved in the `data` directory of the `Combinatorial-Parameters` repository.

5. **Generate the docs**
	- Run this command:
        ```bash
        python3 generate_website.py <Mathematical-Structures>/data/<directory of interest> --output_dir <Mathematical-Structures>/docs/<directory of interest>
        ```
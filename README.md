# Spring 25 CS122_Project
## Project Title: YelpScope

## Authors 
Ji Soo Kim  
Kiet Quan

## Project Description
YelpScope aims to analyze customer feedback and identify key business trends for restaurants based on location and food categories using data from the Yelp Fusion API. By integrating customer reviews, ratings, price ranges, and other key metrics, YelpScope will offer insights into which businesses are performing well and which regions have the highest customer satisfaction. The goal is to provide a comprehensive tool for both consumers and restaurant owners, enabling them to make informed decisions based on up-to-date and detailed data. YelpScope will allow users to sort and filter results based on different criteria, such as ratings, price levels, and review counts, making it easy to spot trends in various locations. The interface will be designed for simplicity and interactivity, offering features like a “Fetch Info” button to pull fresh data from the API and ensure visualizations are always up-to-date. This project will also highlight correlations between various factors, such as the impact of review count on ratings or the most popular cuisines in specific areas.

## Project Outline/Plan
**Interface**
<ul>
    <li>GUI Development
        <ul>
            <li>Programming with TKinter to create a visual and interactive prototype.</li>
            <li>Collaborative Design: The interface will be developed together, ensuring that both design aesthetics and functionality meet our needs.</li>
        </ul>
    </li>
    <li>Prototype Features
        <ul>
            <li>A "Fetch Info" button that recalls the API to update the displayed data.</li>
            <li>Built-in sorting mechanisms and filters to allow users to interact with data (sorting by ratings, review counts, price levels, etc.).</li>
        </ul>
    </li>
</ul>

**Data Collection and Storage Plan:** <br>
The project will gather data from the Yelp Fusion API. This data will contain customer reviews, stars, review counts, etc. This data will then be stored in multiple csv files in a comma-separated format. 

**Data Analysis and Visualization Plan:**
<ul>
    <li>Data Analysis Focus:
        <ul>
            <li>Identify trends such as which state has the most 5-star reviews or the highest number of reviews.</li>
            <li>Explore other potential trends using data from API tables (types of food, 3 reviews, ratings, review count, price levels, address/coordinates)</li>
            <li>Examples: most popular food types by region, average price levels across states</li>
        </ul>
    </li>
    <li>Visualization Approach:
        <ul>
            <li>Create different types of graphs to display trends.</li>
            <li>Implement interactive elements in the GUI using TKinter.</li>
            <li>Use clear and intuitive design elements to make the analysis accessible to users.</li>
        </ul>
    </li>
</ul>

## .gitignore file and a license
This .gitignore file excludes a wide range of automatically generated files from Python development, including byte-compiled files, caches, build artifacts, logs, and virtual environments. It also ignores framework-specific and tooling-related files for projects using Django, Flask, Jupyter, and several packaging and type-checking tools. Manually added to ignore the .DS_Store file that macOS creates automatically to store folder view settings and other metadata. This keeps the project clean of unnecessary files. <br>
**License Type**: BSD 3-Clause "New" or "Revised" License

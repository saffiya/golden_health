<h1>Golden Health</h1>
<a href="https://golden-health.herokuapp.com">Click here to view the site</a>

<h4>This website is orientated on healthy herbal teas that help the immune system. The site is designed to be fully responsive and accessible on a wide range of devices, making it easy to navigate for users. The site has a fully integrated payment system using stripe test mode (please read the checkout section of this read me for more information before testing it out)</h4>

<h2><u>User Experience (UX)</u></h4>
<h3>User Stories:</h4>
<h4>First-time Visitor Goals:</h5>
<ul>
    <li>As a first-time user, I want to easily understand the site's primary purpose and learn more about the products.</li>
    <li>As a first-time user, I want to navigate through the site to find products quickly.</li>
    <li>As a first-time user, I want to be able to create an account easily and sign out</li>
    <li>As a first-time user, I want to be able to read reviews from other users giving me a deeper understanding of the product.</li>
    <li>As a first-time user, I want to be able to use filters and a search bar to find products quicker and alter my search</li>
</ul>
<h4>Returning Visitor Goals:</h4>
<ul>
    <li>As a returning visitor, I want to be able to see what i have purchased in the past</li>
    <li>As a returning visitor, I want to be able to reset my password if i have forgotten it </li>
    <li>As a returning visitor, I want to be able to update my delivery information</li>
</ul>
<h4>Site Owner Goals:</h4>
<ul>
    <li>As the site owner, I want to be able to Add new products to the site</li>
    <li>As the site owner, I want to be able to Edit products currently on the site</li>
    <li>As the site owner, I want to be able to Delete products from the site</li>
</ul>
<h2><u>Design</u></h2>
<h3>Colour Scheme:</h3>
<ul>
    <li>The two primary colours are black and white. I wanted the site to be simple, so the main focus is all on the products.</li>
</ul>
<h3>Imagery:</h3>
<ul>
    <li>Imagery is really important because the colour scheme is so simple it allows the images to be the star of the show. When you go into the site, the first image you see is an image of a transparent mug and cup with herbal tea inside. I love this picture so much because it's bright, simple, and a perfect way of adding more colour to the site while setting the rest of its mood.</li>
    <li>The only other images that are shown throughout the rest of the site are products. I got the products images from google using the licence free to modify, share and use or from adobe stock images that i have purchased. </li>
</ul>

<h3>Wireframes:</h3>
<a href="https://balsamiq.cloud/sqgxjhd/pik9j3d">Click here to view the wireframes i created using Balsamiq</a>

<h2><u>Features</u></h2>
<ul>
    <li>Responsive to all device sizes</li>
    <li>When any products are added to the bag an alert is shown with the updated bag</li>
    <li>Fully functioning checkout system in place using stripe</li>
    <li>Users can log in and out</li>
    <li>Users are able to make reviews</li>
    <li>Users are able to view order history</li>
    <li>Superusers are able to add, edit and delete products</li>
    <li>Fully functioning emails sent out</li>
</ul>

<h2><u>Technologies Used</u></h2>
<h3>Languages Used:</h3>
<ul>
    <li>HTML5</li>
    <li>Python</li>
    <li>JavaScript</li>
    <li>CSS</li>
</ul>
<h3>Frameworks, Libraries & Programs Used:</h3>
<ul>
    <li>Bootstrap was used to assist with the responsiveness and styling of the website</li>
    <li>Google Fonts were used to import the fonts used throughout the site</li>
    <li>Font Awesome was used to add icons to the site such as the search icon, the bag icon, the person icon etc.</li>
    <li>jQuery came with the bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript</li>
    <li>Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to Github</li>
    <li>Github is used to store the project's code after being pushed from Git</li>
    <li>Balsamiq was used to create the wireframes during the design process</li>
    <li>AWS was used for S3 storage</li>
    <li>Gmail was used to send emails from the site to customers</li>
    <li>Stripe was used in checkout giving the ability to process payments</li>
    <li>Adobe Stock was used to acquire specific images. Images such as the hompage image were purchased through Adobe Stock</li>
    <li>Photoshop was used to resize some images</li>
</ul>
<h2><u>Checkout</u></h2>
<p>The Stripe functionality within the site is only for testing. Please use 4242 4242 4242 4242 as the card number, 04/24 as the expiry date, 242 as the CVC and 42424 as the ZIP.</p>

<h2><u>Testing</u></h2>
<h3>Testing User Stories from User Experience (UX) Section</h3>
<h4>First Time Visitor Goals:</h4>

<h5>As a first-time visitor, I want to easily understand the site's primary purpose and learn more about the products.</h5>

<ul>
    <li>Upon entering the site, users are automatically greeted with a clean and easily readable navigation bar to go the page of their choice and a search bar to go straight to the product of their choice. Underneath there is an Image with the text "Explore our wide range of teas" and a "Shop Now" call to action button.
    </li>
    <li>The title makes it clear what the primary purpose of the site is </li>
    <li>The user has two options, click the call to action button or use the navigation buttons to view the products.</li>
    <li>When the user clicks into each product, there is a summary of the product allowing them to learn more about it.</li>
</ul>

<h5>As a first-time visitor, I want to navigate throughout the site to find products quickly.</h5>

<ul>
    <li>The site has been designed to be fluid and never to entrap the user. There is a clean navigation bar at the top of each page; each link describes what page they will end up at. The navigation is fixed on the screen so no matter how far down the screen the user scrolls, they will never be stuck.</li>
    <li>There is a button to take the user back to the top of the page on all screens at the bottom right-hand side on the All Products, Tea and Teaware pages. So the user doesn't feel trapped when they get to the bottom of the page. On smaller screens the button also appears in checkout.</li>
    <li>The site has a search bar so the user can easily find any product they want effortlessly.</li>
    <li>On each products page, there is a filtering system so users can sort by: Price, Rating, Name, Category</li>
</ul>

<h5>As a first time user, I want to be able to create an account easily and sign out</h5>

<ul>
    <li>By clicking on the My Account icon, users can register or log in </li>
    <li>The user is easily able to register an account by simply filling in the form which asks for their email, username and password. Once the form has been filled out they will recieve a verification email. Once they have clicked the link to verify their account, there profile will be up and running.</li>
    <li>Once the user is logged in the My Account icon changes to give the user the ability to view their profile or logout. Once logout is clicked to verify the user does indeed want to logout they are taken to a page which allows them to cancel and go back or press sign out which will log them out and return the user to the home page</li>
</ul>

<h5>As a first time user, I want to be able to read reviews from other users giving me a deeper understanding of the product</h5>

<ul>
    <li>Once the user clicks on the product they like, it takes them to a product page which shows, the product, product description, rating and reviews.</li>
    <li>The reviews on the products pages are made by customers who have purchased from the company before.</li>
</ul>

<h5>As a first time user, I want to use filters and a search bar to find products quicker and alter my search. </h5>

<ul>
    <li>No matter what page you are on the search bar is always there at the top of the page, allowing users to find products quicker.</li>
    <li>When searching through the product pages, there is a sort by the filter at the top right of the screen allowing users to adapt the filter to show what they want to be displayed first whether it be sorting them by name, price, rating or category—thus allowing users to alter their search.</li>
</ul>

<h4>Returning Visitor Goals:</h4>

<h5>As  a returning visitor, I want to be able to log in and out of my account easily</h5>

<ul>
    <li>Users can easily log in using the My Account icon, which gives them two options to log in or register. Returning visitors can click login and use their username and password to log in. </li>
    <li>My favourite feature is the remember me box, which is excellent for returning users. Once Remember me is pressed their login details will come up automatically making the login process even more comfortable.</li>
    <li>The site is made to be as simple to use as possible. I wanted users to log in and out just as quickly as moving from one page to another. </li>
    <li>Once the user is logged in the My Account icon changes to give the user the ability to view their profile or logout, once log out is clicked to verify the user does indeed want to logout they are taken to a page which allows them to cancel and go back or press sign out which will log them out and return the user to the home page. </li>
</ul>

<h5>As a returning visitor, I want to be able to see what I have purchased in the past</h5>

<ul>
    <li>When a user is logged in, if they click the My Account icon, it will show two options My Profile and Logout. If they click My Profile, it will take the user to their profile where they can see their order history. If they click on the order number, it will take them to their full order if they need to review the entire order.</li>
</ul>

<h5>As a returning visitor,  I want to make reviews on products I have purchased.</h5>

<ul>
    <li>If the user clicks on the product, they want to review and clicks on the Make Review button In the reviews section, they will be redirected to a review form they can fill out.</li>
</ul>

<h5>As a returning visitor, I want to be able to reset my password if I have forgotten it </h5>

<ul>
    <li>When a user is logging in, there is a link called "Forgot Password?" when clicked the user is redirected to a page called Password Reset which allows the user to reset their password by entering their email address</li>
</ul>

<h5>As a returning visitor, I want to be able to update my delivery information</h5>

<ul>
    <li>When a user is logged in if they go to their profile, there is a form showing their current default delivery address. They can change whatever they need to change and press the Update Information button to update it.</li>
</ul>

<h4>Site Owner Goals:</h4>

<h5>As the site owner,  I want to be able to add new products to the site</h5>

<ul>
    <li>When the superuser is logged in the My Account icon when clicked will show three options: Product Management, My Profile, Log Out <br> When Product Management is clicked, the user will be redirected to a page where they can add a product by filling a form with the following: Category, SKU, Name, Description Title, Description, Has Sizes, How to use, Price, Rating and Image URL the user also has the option to select an image from there computer by clicking on the select image button. 
    </li>
</ul>

<h5>As the site owner, I want to be able to edit products currently on the site</h5>

<ul>
    <li>When the superuser is logged in. If they click on the products page they, unlike normal users, will have two buttons near the rating of each product one called 'Edit' and the other called 'Delete'.  Once Edit is clicked the user is redirected to a page called 'Edit a Product' where there is a form pre-filled with all the products information, the user can edit whatever they want then press the Update Product button. 
    </li>
</ul>

<h5>As the site owner,  I want to be able to delete products currently on the site</h5>

<ul>
    <li>When the superuser is logged in, if they click on the products page they, unlike normal users, will have two buttons near the rating of each product one called 'Edit' and the other called 'Delete'.  Once Edit is clicked the user is redirected to a page called 'Edit a Product' where there is a form pre-filled with all the products information, the user can edit whatever they want then press the Update Product button. 
    </li>
</ul>

<h2><u>Known Bugs</u></h2>

<ul>
    <li>In heroku when going to checkout, the payment section is not showing;and when going to pay an error occurs. Even though stripe is fully functioning. The stripe function has worked perfectly in the past, but at the time of writing this heroku is showing an error.</li>
</ul>

<h2><u>Deployment</u></h2>
<h3>Heroku</h3>
<p>The project was developed using Gitpod, commited to git and pushed to Github. My GitHub is linked with Heroku, so anything i pushed to GitHub automatically got deployed to Heroku. I used AWS S3 as storage. When i pushed my code to Heroku i had to make sure all my static files were in my storage AWS S3 as otherwise none of my images or CSS would show. </p>

<h3>Making a Local Clone</h3>
<ul>
    <li>Log in to Githun and locate the GitHub Repository</li>
    <li>Under the repository name (golden_health), click the "Clone or download"</li>
    <li>To clone the repository using HTTPS, under "Clone with HTTPS" copy the link.</li>
    <li>In your local IDE open Git Bash</li>
    <li>Change the current working directory to the location where you want the cloned directory to be made</li>
    <li>Type git clone, and then paste the URL you copied from the clone in the HTTP's section <br>
    git clone https://github.com/saffiya/golden_health.git
    </li>
    <li>Press Enter. Your local clone will be created</li>
</ul>
<a href="https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository">Click here for more information on the above process </a>

<h2><u>Credits</u></h2>
<h3>Code</h3>
<ul>
    <li>Bootstrap is used throughout the project to make the site more responsive</li>
    <li>Balsamiq is my favourite site for making wireframes and is the site i used for this projects wireframes</li>
    <li>AWS S3 is used for storage </li>
    <li>Code institute full stack development videos were a big help in the development of this project</li>
    <li>Font Awesome was used for icons</li>
    <li>Google Fonts was used for the fonts used throughout the site</li>
    <li>For help in figuring out the layout of this read me i followed the Code-institute-Solutions sample README</li>
</ul>
<h3>Media</h3>
<p>I used Adobe Stock to but some images used in the site. I also got images from google using the free to use and modify license and i also got some from freepik.</p>

<h3>Acknowledgements</h3>
<ul>
    <li>The tutor support team for all the help when i got stuck</li>
    <li>I looked to vlad opreas code on dream woolies for the implementation of some of the review section used in my project</li>
    <li>My mentor for continuous helpful feedback.</li>
</ul>



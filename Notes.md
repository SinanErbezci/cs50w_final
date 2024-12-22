get_object_or_404 -> gets the objects. If three is no object it raises 404.

Always return an HttpResponseRedirect after successfully dealing
with POST data. This prevents data from being posted twice if a
user hits the Back button.

# Query expressions.
F() expressions. Directly doing database manupilations. No loading data to python and make changes etc.
getting the database, rather than Python, to do work
reducing the number of queries some operations require
reporter = Reporters.objects.get(name="Tintin")
reporter.stories_filed = F("stories_filed") + 1
reporter.save()

# Generic views
These views represent a common case of basic web development: getting data from the database according to a parameter passed in the URL, loading a template and returning the rendered template. Because this is so common, Django provides a shortcut, called the “generic views” system.

path("<int:pk>") -> pk necessary for generic views


        <!-- <nav class="navbar navbar-expand-lg justify-content-between flex-nowrap py-2 py-lg-0">
            <div class="container nav-contain p-2 ms-4 me-4">
                <a href="{% url 'index' %}"><img class="brand-img me-4" src="{% static 'library/images/svg.svg'%}" alt="logo"></a>
                <div class="container search-bar search-bar-loading">
                    <div class="input-group search-bar-input">
                        <input class="form-control" type="search" placeholder="Search" aria-label="Search">
                        <button class="btn search-btn" type="submit"><i class="fa-solid fa-magnifying-glass"></i></button>
                    </div>
                    <div class="search-bar-results">
                        <a href="" class="search-result">
                            <div class="search-result-title">First Last Name</div>
                            <p class="search-result-paragraph">Lorem ipsum dolor sit amet consectetur adipisicing elit. Eius, modi voluptates praesentium animi voluptatibus tempore. Iste corporis id eaque? Aliquam eius praesentium debitis, consectetur dolor recusandae repellat atque sequi necessitatibus.</p>
                        </a>
                        <a href="" class="search-result">
                            <div class="search-result-title">First Last Name</div>
                            <p class="search-result-paragraph">Lorem ipsum dolor sit amet consectetur adipisicing elit. Eius, modi voluptates praesentium animi voluptatibus tempore. Iste corporis id eaque? Aliquam eius praesentium debitis, consectetur dolor recusandae repellat atque sequi necessitatibus.</p>
                        </a>
                    </div>
                </div>

                <button class="navbar-toggler border-0" type="button" data-bs-toggle="offcanvas" data-bs-target="#top-navbar" aria-controls="top-navbar">
                    <span class="navbar-toggler-icon"></span>
                </button>
                
                <div class="offcanvas offcanvas-end" tabindex="-1" id="top-navbar" aria-labelledby="top-navbarLabel">
                    <button class="navbar-toggler border" type="button" data-bs-toggle="offcanvas" data-bs-target="#top-navbar" aria-controls="top-navbar">
                        <div class="d-flex justify-content-between p-3">
                            <img class="brand-img" src="{% static 'library/images/svg.svg' %}" alt="logo">
                            <span class="navbar-toggler-icon"></span>
                        </div>
                    </button>
                    {% if user.is_authenticated %}
                    <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">Browse</a>
                            <div class="dropdown-menu">
                                <div class="row">
                                    <div class="d-flex nav-options">
                                    <a class="dropdown-item" href="#">Books</a>
                                    <a class="dropdown-item" href="#">Authors</a>
                                    <a class="dropdown-item" href="#">Lists</a>
                                    <a class="dropdown-item" href="#">Genres</a>
                                    </div>
                                </div>  
                            </div>
                            <li class="nav-item dropdown">
                                <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false"><i class="fa-solid fa-user"></i></a>
                                <div class="dropdown-menu">
                                    <div class="row">
                                        <div class="d-flex nav-options">
                                        <a class="dropdown-item" href="#">Profile</a>
                                        <a class="dropdown-item" href="#">My Books</a>
                                        <a class="dropdown-item" href="#">Reading Challenge</a>
                                        </div>
                                    </div>  
                                </div>
                              </li>
                              <li class="nav-item dropdown">
                                <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false"><i class="fa-solid fa-users"></i></a>
                                <div class="dropdown-menu">
                                    <div class="row">
                                        <div class="d-flex nav-options">
                                        <a class="dropdown-item" href="#">Messages</a>
                                        <a class="dropdown-item" href="#">Friends</a>
                                        <a class="dropdown-item" href="#">Groups</a>
                                        </div>
                                    </div>  
                                </div>
                              </li>
                              <li class="nav-item">
                                <a class="nav-link" href="{% url 'logout' %}"><i class="fa-solid fa-arrow-right-from-bracket"></i></a>
                              </li>
                    </ul>
                    {% else %}
                    <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">Browse</a>
                            <div class="dropdown-menu">
                                <div class="row">
                                    <div class="d-flex nav-options">
                                    <a href="{% url 'browse' %}" class="dropdown-item" href="#">Books</a>

                                    </div>
                                </div>  
                            </div>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link nav-login" href="{% url 'login' %}">Log In</a>
                        </li>
                    </ul>
                    {% endif %}
                </div>
            </div>
        </nav>
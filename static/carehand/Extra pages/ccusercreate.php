<?php 
  include('createrc.php')
  session_start(); 

  if (!isset($_SESSION['username'])) {
    session_destroy();
    unset($_SESSION['username']);
    $_SESSION['msg'] = "You must log in first";
    header('location: rclogin.php');
  }
  if (isset($_GET['logout'])) {
    session_destroy();
    unset($_SESSION['username']);
    header("location: rclogin.php");
  }
?>
<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>CareHand</title>
    <link rel="icon" href="img/favicon.png">
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <!-- animate CSS -->
    <link rel="stylesheet" href="css/animate.css">
    <!-- owl carousel CSS -->
    <link rel="stylesheet" href="css/owl.carousel.min.css">
    <!-- themify CSS -->
    <link rel="stylesheet" href="css/themify-icons.css">
    <!-- flaticon CSS -->
    <link rel="stylesheet" href="css/flaticon.css">
    <!-- magnific popup CSS -->
    <link rel="stylesheet" href="css/magnific-popup.css">
    <!-- nice select CSS -->
    <link rel="stylesheet" href="css/nice-select2.css">
    <!-- swiper CSS -->
    <link rel="stylesheet" href="css/slick.css">
    <!-- style CSS -->
    <link rel="stylesheet" href="css/style2.css">
    <link rel="stylesheet" href="css/style.css">
     <link rel="stylesheet" href="block/css/main.css" />
    <link rel="stylesheet" href="block/css/main2.css" />
</head>

<body>
    <!--::header part start::-->
    <header class="main_menu home_menu">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-12">
                    <nav class="navbar navbar-expand-lg navbar-light">
                        <a class="navbar-brand" href="#"> <img src="img/favicon.png" alt="logo"> </a><h3><font color="#fff">CareHand</font></h3>
                        <button class="navbar-toggler" type="button" data-toggle="collapse"
                            data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
                            aria-expanded="false" aria-label="Toggle navigation">
                            <span class="ti-menu"></span>
                        </button>

                        <div class="collapse navbar-collapse main-menu-item justify-content-end"
                            id="navbarSupportedContent">
                            <ul class="navbar-nav align-items-center">
                                
                                    <li class="nav-item dropdown">
                                    <a class="nav-link dropdown-toggle" href="blog.html" id="navbarDropdown"
                                        role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                        Collection Center
                                    </a>
                                    <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                                       
                                        <a class="dropdown-item" href="#">Create</a>
                                        
                                    </div>
                                </li>
                                
                                
                               <li class="nav-item dropdown">
                                    <a class="nav-link dropdown-toggle" href="blog.html" id="navbarDropdown_1"
                                        role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                         <font color="white"><?php echo htmlspecialchars($_SESSION["username"]); ?></font>
                                    </a>
                                    <div class="dropdown-menu" aria-labelledby="navbarDropdown_2">
                                        <a href="rclogin.php?logout='1'"  class="dropdown-item"> logout</a> 
                                        
                                    </div>
                                </li>
                            </ul>
                        </div>
                    </nav>
                </div>
            </div>
        </div>
        <!-- Header -->
            <header id="header" class="alt">
               <a href="#"></a>
                
            </header>
    </header>
    <!-- Header part end-->

<!-- intro_video_bg start-->
    <section class="intro_video_bg">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-md-8 col-lg-6">
                    <div class="intro_video_iner text-center">
                        <h2></h2>
                       
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- intro_video_bg part start-->


    <!-- reg_part start-->
    <section id="two" class="wrapper style2">
                <div class="inner">
                    <div class="box">
                        <div class="content">
                            <header class="align-center">
                                <p>Here You Can</p>
                                <h2>Register Your Collection Center</h2>
                            </header>
                            <div class="header">
                            <h2>Register</h2>
                            </div>
  
                                 <form name="createrc" method="post" action="ccusercreate.php" enctype="multipart/form-data">
                                        <?php include('errors.php'); ?>

                                          
                                           <div class="input-group">
                                              <label>Name Of Center</label>      <input type="text" name="rcname" id="rcname"  required><br>
                                           </div>

                                           <div class="input-group">
                                                  <label>Person In Charge</label><input type="text" name="rccharge" id="pic"   required ><br>
                                           </div>


                                           <div class="input-group">
                                             <label>Contact No</label>           <input type="number" name="contact" id="ph"   required style="background-color: #ececec; border:1px solid #c9c9c9" ><br><br>
                                           </div>

                                           <div class="input-group">
                                             <label>State</label>&nbsp;&nbsp;

                                            <div class="form-select" id="default-select_1">
                                             <select name="states" id="state" size="1" onchange="select()" >
                                                <option value="" selected="selected">Select State</option>
                                                <option value="Kerala">Kerala</option>
                                                <option value="Tamilnadu">Tamilnadu</option>
                                                <option value="Karnatka">Karnatka</option>
                                                <option value="Goa">Goa</option>
                                             </select><br><br>
                                           </div>

                                       </div>
                                           <div class="input-group">
                                             <label>District</label>&nbsp;&nbsp;
                                             <div class="form-select" id="district">
                                                                                                                                                        
                                            </div>
                                           </div>
                                           <div><br></div>
                                           <div class="input-group">
                                             <label>Address</label>                <input type="text" name="address" id="address"   required><br><br><br><br>
                                           </div>
                                           <div class="input-group">
                                             <label>Supply Requirements:</label><br><br>
                                           </div>



                                             <div class="input-group"><button type="submit" class="btn" name="reg_user">Register</button><br></div>
                                           
                                 </form>
                        </div>
                        </div>
                        </div>
                    </section>
    <!-- reg_part start-->
    
    <!--::our client part start::-->
    <section class="client_part section_padding">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-xl-8">
                    <div class="section_tittle text-center">
                        <p></p>
                        <h2></h2>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!--::our client part end::-->

   <!-- footer part start-->
    <footer class="footer-area">
        <div class="container">
            <div class="row justify-content-between">
                <div class="col-sm-6 col-md-4 col-xl-3">
                    <div class="single-footer-widget footer_1">
                        <a href="index.php"> <img src="img/favicon.png" alt=""> </a><font color="#fff">CareHand</font>
                        <p>A webportal which helps the peoples to easily
                        find out where the relief centers and collection
                        centers are placed,and donate requirements they needed.They can register as a volunteer.
                            </p>
                    </div>
                </div>
               
                <div class="col-xl-3 col-sm-6 col-md-4">
                    <div class="single-footer-widget footer_2">
                        <h4>Contact us</h4>
                        <p>D3 BCA ,St Mary's College, Sulthan Bathery,Wayanad,Kerala</p>
                        <div class="contact_info">
                            <p><span class="ti-mobile"></span> +91 9567834429</p>
                            <p><span class="ti-email"></span>reliefproject@gmail.com </p>
                            <p><span class="ti-world"></span>reliefcell.com </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="container-fluid">
            <div class="row">
                <div class="col-lg-12">
                    <div class="copyright_part_text text-center">
                        <div class="row">
                            <div class="col-lg-12">
                                <p class="footer-text m-0">
Copyright &copy;<script>document.write(new Date().getFullYear());</script> All rights reserved
</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </footer>
    <!-- footer part end-->
    
    <!-- jquery plugins here-->

    <script src="js/jquery-1.12.1.min.js"></script>
    <!-- popper js -->
    <script src="js/popper.min.js"></script>
    <!-- bootstrap js -->
    <script src="js/bootstrap.min.js"></script>
    <!-- easing js -->
    <script src="js/jquery.magnific-popup.js"></script>
    <!-- swiper js -->
    <script src="js/swiper.min.js"></script>
    <script src="js/wow.min.js"></script>
    <script src="js/jquery.smooth-scroll.min.js"></script>
    <!-- swiper js -->
    <script src="js/masonry.pkgd.js"></script>
    <!-- particles js -->
    <script src="js/owl.carousel.min.js"></script>
    <script src="js/jquery.nice-select.min.js"></script>
    <!-- swiper js -->
    <script src="js/slick.min.js"></script>
    <script src="js/jquery.counterup.min.js"></script>
    <script src="js/waypoints.min.js"></script>
    <!-- contact js -->
    <script src="js/jquery.ajaxchimp.min.js"></script>
    <script src="js/jquery.form.js"></script>
    <script src="js/jquery.validate.min.js"></script>
    <script src="js/mail-script.js"></script>
    <script src="js/contact.js"></script>
    <!-- custom js -->
    <script src="js/custom.js"></script>
    <script src="js/selectstate.js"></script>
</body>

</html>
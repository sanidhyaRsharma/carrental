import React from "react";
import { Routes, Route, Navigate } from "react-router-dom";
import Home from "../Pages/Home"
import SignUp from "../Pages/signUp";
import UserAuth from "../Pages/signIn"
import SignIn from "../Pages/signIn";
// import About from "../pages/About";
// import CarListing from "../pages/CarListing";
// import CarDetails from "../pages/CarDetails";
// import Blog from "../pages/Blog";
// import BlogDetails from "../pages/BlogDetails";
// import NotFound from "../pages/NotFound";
// import Contact from "../pages/Contact";


const Routers = () => {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/signIn" />} />
      <Route path="/home" element={<Home />} />
      <Route path="/UserAuth" element={<UserAuth />}/>
      <Route path="/signIn" element={<SignIn />}/>
      <Route path="/signUp" element={<SignUp />}/>
      {/* <Route path="/about" element={<About />} />
      <Route path="/cars" element={<CarListing />} />
      <Route path="/cars/:slug" element={<CarDetails />} />
      <Route path="/blogs" element={<Blog />} />
      <Route path="/blogs/:slug" element={<BlogDetails />} />
      <Route path="/contact" element={<Contact />} />
      <Route path="*" element={<NotFound />} /> */}
    </Routes>
  );
};

export default Routers;

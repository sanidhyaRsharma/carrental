import React from "react";

import { Container } from "reactstrap";
import { NavLink } from "react-router-dom";
import "../styles/header.css";
// import Button from "@mui/material/Button";

const navLinks = [
  {
    path: "/home",
    display: "Home",
  },
  {
    path: "/about",
    display: "About",
  },
  {
    path: "/cars",
    display: "Cars",
  },

  {
    path: "/blogs",
    display: "Blog",
  },
  {
    path: "/contact",
    display: "Contact",
  },
];

const Header = () => {
  return (
    <header className="header">
      <div className="main__navbar">
        <Container>
          <div className="d-flex align-items-center justify-content-between">
            <div className="menu">
              {navLinks.map((item, index) => (
                <NavLink
                  to={item.path}
                  className={(navClass) =>
                    navClass.isActive ? "nav__active nav__item" : "nav__item"
                  }
                  key={index}
                >
                  {item.display}
                </NavLink>
              ))}
            </div>
            {/* <Button
              href="/signIn"
              variant="contained"
              type="submit"
              sx={{ mt: 3, mb: 2 }}
            >
              Login / SignUp
            </Button> */}
          </div>
        </Container>
      </div>
    </header>
  );
};

export default Header;

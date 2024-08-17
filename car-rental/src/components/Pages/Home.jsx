import React from "react";
import Helmet from "../Helmet/Helmet";
import { Container, Row } from "reactstrap";
import FindCarForm from "../UI/FindCarForm";
import SimpleMap from "./Map";

const Home = () => {
  return (
    <Helmet title="Home">
      <div className="hero__form">
        <Container>
          <Row className="form__row">
            <FindCarForm />
          </Row>
        </Container>
        <Container>
          <SimpleMap />
        </Container>
      </div>
    </Helmet>
  );
};

export default Home;

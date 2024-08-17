import React from "react";
import "../styles/find-car-form.css";
import { Form, FormGroup } from "reactstrap";
import dayjs from "dayjs";
import TextField from "@mui/material/TextField";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";
import { LocalizationProvider } from "@mui/x-date-pickers/LocalizationProvider";
import { DateTimePicker } from "@mui/x-date-pickers/DateTimePicker";
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import Select from "@mui/material/Select";
import FormControl from "@mui/material/FormControl";
import Button from "@mui/material/Button";

const FindCarForm = () => {
  const [value, setValue] = React.useState(dayjs());
  const [carType, setcarType] = React.useState("");

  const handleChange = (event) => {
    setcarType(event.target.value);
  };
  return (
    <Form className="form">
      <div className=" d-flex align-items-center justify-content-between flex-wrap">
        <FormGroup className="form__group">
          <FormControl sx={{ m: 1, minWidth: 250 }} size="large">
            <TextField
              id="outlined-search"
              label="Pick-up Location"
              type="search"
              fullWidth
              margin="normal"
              required
            />
          </FormControl>
        </FormGroup>

        <FormGroup className="form__group">
          <FormControl sx={{ m: 1, minWidth: 250 }} size="large">
            <LocalizationProvider dateAdapter={AdapterDayjs}>
              <DateTimePicker
                renderInput={(props) => <TextField {...props} />}
                label="Pick-up Date & Time"
                style={{ width: 100 }}
                value={value}
                onChange={(newValue) => {
                  setValue(newValue);
                }}
              />
            </LocalizationProvider>
          </FormControl>
        </FormGroup>

        <FormGroup className="form__group">
          <FormControl sx={{ m: 1, minWidth: 250 }} size="large">
            <LocalizationProvider dateAdapter={AdapterDayjs}>
              <DateTimePicker
                renderInput={(props) => <TextField {...props} />}
                label="Drop-off Date & Time"
                value={value}
                onChange={(newValue) => {
                  setValue(newValue);
                }}
              />
            </LocalizationProvider>
          </FormControl>
        </FormGroup>

        <FormGroup className="form__group">
          <FormControl sx={{ m: 1, minWidth: 250 }} size="large">
            <TextField
              id="outlined-search"
              label="Drop Location"
              type="search"
              fullWidth
              margin="normal"
              required
            />
          </FormControl>
        </FormGroup>
        <FormGroup className="select__group">
          <FormControl sx={{ m: 1, minWidth: 250 }} size="large">
            <InputLabel id="demo-select-small">Car Type</InputLabel>
            <Select
              labelId="demo-select-small"
              id="demo-select-small"
              value={carType}
              label="CarType"
              onChange={handleChange}
            >
              <MenuItem value="">
                <em>None</em>
              </MenuItem>
              <MenuItem value={10}>SUV</MenuItem>
              <MenuItem value={20}>Sedan</MenuItem>
              <MenuItem value={30}>Hatchback</MenuItem>
              <MenuItem value={40}>Electric</MenuItem>
            </Select>
          </FormControl>
        </FormGroup>

        <FormGroup className="form__group">
          <FormControl sx={{ m: 1, minWidth: 100 }} size="small">
            <Button
              variant="contained"
              type="submit"
              fullWidth
              sx={{ mt: 3, mb: 2 }}
            >
              Find Car
            </Button>
          </FormControl>
        </FormGroup>
      </div>
    </Form>
  );
};

export default FindCarForm;

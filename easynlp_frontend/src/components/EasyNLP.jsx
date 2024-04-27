import * as React from "react";
import { styled, useTheme } from "@mui/material/styles";
import Box from "@mui/material/Box";
import Drawer from "@mui/material/Drawer";
import CssBaseline from "@mui/material/CssBaseline";
import MuiAppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import List from "@mui/material/List";
import Typography from "@mui/material/Typography";
import Divider from "@mui/material/Divider";
import IconButton from "@mui/material/IconButton";
import MenuIcon from "@mui/icons-material/Menu";
import ChevronLeftIcon from "@mui/icons-material/ChevronLeft";
import ChevronRightIcon from "@mui/icons-material/ChevronRight";
import ListItem from "@mui/material/ListItem";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemText from "@mui/material/ListItemText";
import { Button } from "@mui/material";
import TextField from "@mui/material/TextField";
import axios from "axios";
import CloudUploadIcon from '@mui/icons-material/CloudUpload';

const VisuallyHiddenInput = styled('input')({
  clip: 'rect(0 0 0 0)',
  clipPath: 'inset(50%)',
  height: 1,
  overflow: 'hidden',
  position: 'absolute',
  bottom: 0,
  left: 0,
  whiteSpace: 'nowrap',
  width: 1,
});

const drawerWidth = 240;

const Main = styled("main", { shouldForwardProp: (prop) => prop !== "open" })(
  ({ theme, open }) => ({
    flexGrow: 1,
    padding: theme.spacing(3),
    transition: theme.transitions.create("margin", {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    }),
    marginLeft: `-${drawerWidth}px`,
    ...(open && {
      transition: theme.transitions.create("margin", {
        easing: theme.transitions.easing.easeOut,
        duration: theme.transitions.duration.enteringScreen,
      }),
      marginLeft: 0,
    }),
  })
);

const AppBar = styled(MuiAppBar, {
  shouldForwardProp: (prop) => prop !== "open",
})(({ theme, open }) => ({
  transition: theme.transitions.create(["margin", "width"], {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen,
  }),
  ...(open && {
    width: `calc(100% - ${drawerWidth}px)`,
    marginLeft: `${drawerWidth}px`,
    transition: theme.transitions.create(["margin", "width"], {
      easing: theme.transitions.easing.easeOut,
      duration: theme.transitions.duration.enteringScreen,
    }),
  }),
}));

const DrawerHeader = styled("div")(({ theme }) => ({
  display: "flex",
  alignItems: "center",
  padding: theme.spacing(0, 1),
  // necessary for content to be below app bar
  ...theme.mixins.toolbar,
  justifyContent: "flex-end",
}));

export default function PersistentDrawerLeft() {
  const theme = useTheme();
  const [open, setOpen] = React.useState(true);
  const [input, setInput] = React.useState("");
  const [output, setOutput] = React.useState("");
  const [image, setImage] = React.useState("");

  const group1 = [
    { text: "Tokenization", key: "tokenize" },
    { text: "Stopword Removal", key: "remove_stopwords" },
    { text: "Lowercasing", key: "lowercasing" },
    { text: "Contractions", key: "handle_contractions" },
    { text: "Stemming", key: "stem" },
    { text: "Lemmitization", key: "lemmatization" },
    { text: "Remove Text Outliers", key: "remove_text_outliers" },
    { text: "Stemming", key: "stem" },
  ];
  const group2 = [
    { text: "Counting Word Frequencies", key: "word_freq_analysis" },
    { text: "Visualizing Word Frequencies", key: "word_cloud" },
  ];
  const group3 = [
    { text: "POS Tagging", key: "pos_tagging" },
    { text: "Sentiment Analysis", key: "sentiment_analysis" },
  ];
  const group4 = [
    { text: "Named Entity Recognition", key: "ner" },
  ];
  const [selectedText, setSelectedText] = React.useState(group1[0]);

  // React.useEffect(() => {
  //   if(image){
  //     console.log("image: ",image);
  //     const base64Image = base64.fromByteArray(Buffer.from(image));
  //     setUrl(base64Image);
  //   }

  // }, [image]);

  React.useEffect(() => {
    setOutput("");
    setImage("");
  }, [selectedText]);

  const handleDrawerOpen = () => {
    setOpen(true);
  };

  const handleDrawerClose = () => {
    setOpen(false);
  };

  const handleAnalyze = () => {
    setOutput("");
    setImage("");
    // selectedText.text === "Tokenization"
    //   ?
    axios
      .post("http://127.0.0.1:5000/" + selectedText.key, {
        text: input,
      })
      .then(function (response) {
        console.log(response);
        selectedText.key === "word_cloud"
          ? setImage(response.data)
          : setOutput(JSON.stringify(response.data));
      })
      .catch(function (error) {
        console.log(error);
      });
    // : axios
    //     .post("http://127.0.0.1:5000/word_cloud", {
    //       text: input,
    //     })
    //     .then(function (response) {
    //       console.log(response);
    //       // const blob = new Blob([response.data], { type: 'image/png' });
    //       // Generate a URL for the Blob
    //       // const imageUrl = URL.createObjectURL(blob);
    //       // Set the generated URL as the image source
    //       // const byteData = new Uint8Array([
    //       //   response.data
    //       // ]);

    //       // Convert the byte data to a Blob
    //       // const blob = new Blob([byteData], { type: "image/png" });
    //       // const byteData = new Uint8Array([response.data]);

    //       // // Convert the byte data to a string
    //       // const binaryString = String.fromCharCode.apply(null, byteData);

    //       // // Convert the binary string to base64
    //       // const base64ImageData = btoa(binaryString);
    //       // Convert the byte data to a string
    //       const binaryString = unescape(encodeURIComponent(response.data));

    //       // Convert the binary string to base64
    //       const base64ImageData = btoa(binaryString);
    //       console.log("base64ImageData: ", base64ImageData);
    //       setImage(base64ImageData);
    //     })
    //     .catch(function (error) {
    //       console.log(error);
    //     });
  };

  return (
    <Box sx={{ display: "flex" }}>
      <CssBaseline />
      <AppBar position="fixed" open={open}>
        <Toolbar>
          <IconButton
            color="inherit"
            aria-label="open drawer"
            onClick={handleDrawerOpen}
            edge="start"
            sx={{ mr: 2, ...(open && { display: "none" }) }}
          >
            <MenuIcon />
          </IconButton>
          <Typography variant="h6" noWrap component="div">
            EasyNLP
          </Typography>
        </Toolbar>
      </AppBar>
      <Drawer
        sx={{
          width: drawerWidth,
          flexShrink: 0,
          "& .MuiDrawer-paper": {
            width: drawerWidth,
            boxSizing: "border-box",
          },
        }}
        variant="persistent"
        anchor="left"
        open={open}
      >
        <DrawerHeader>
          <IconButton onClick={handleDrawerClose}>
            {theme.direction === "ltr" ? (
              <ChevronLeftIcon />
            ) : (
              <ChevronRightIcon />
            )}
          </IconButton>
        </DrawerHeader>
        <Divider />
        <Typography variant="h6">Text Preprocessing</Typography>
        <Divider />
        <List>
          {group1.map((item, index) => (
            <ListItem key={item.key} disablePadding>
              <ListItemButton
                onClick={() => setSelectedText(item)}
                selected={item.text === selectedText.text}
              >
                {item.text === selectedText.text ? (
                  <ListItemText primary={item.text} />
                ) : (
                  <ListItemText secondary={item.text} />
                )}
              </ListItemButton>
            </ListItem>
          ))}
        </List>
        <Divider />
        <Typography variant="h6">Word Frequency</Typography>
        <Divider />
        <List>
          {group2.map((item, index) => (
            <ListItem key={item.key} disablePadding>
              <ListItemButton
                onClick={() => setSelectedText(item)}
                selected={item.text === selectedText.text}
              >
                {item.text === selectedText.text ? (
                  <ListItemText primary={item.text} />
                ) : (
                  <ListItemText secondary={item.text} />
                )}
              </ListItemButton>
            </ListItem>
          ))}
        </List>
        <Divider />
        <Typography variant="h6">Sentiment Analysis</Typography>
        <Divider />
        <List>
          {group3.map((item, index) => (
            <ListItem key={item.key} disablePadding>
              <ListItemButton
                onClick={() => setSelectedText(item)}
                selected={item.text === selectedText.text}
              >
                {item.text === selectedText.text ? (
                  <ListItemText primary={item.text} />
                ) : (
                  <ListItemText secondary={item.text} />
                )}
              </ListItemButton>
            </ListItem>
          ))}
        </List>
        <Divider />
        <Typography variant="h6">Entity Recognition</Typography>
        <Divider />
        <List>
          {group4.map((item, index) => (
            <ListItem key={item.key} disablePadding>
              <ListItemButton
                onClick={() => setSelectedText(item)}
                selected={item.text === selectedText.text}
              >
                {item.text === selectedText.text ? (
                  <ListItemText primary={item.text} />
                ) : (
                  <ListItemText secondary={item.text} />
                )}
              </ListItemButton>
            </ListItem>
          ))}
        </List>
      </Drawer>
      <Main open={open}>
        <DrawerHeader />
        <div
          style={{
            position: "relative",
            top: "100px",
            display: "flex",
            justifyContent: "space-around",
          }}
        >
          <div
            style={{
              display: "flex",
              gap: "50px",
            }}
          >
            <div style={{ display: "flex", flexDirection: "column" }}>
              <Typography
                style={{ right: "40%", position: "relative" }}
              ></Typography>
              <TextField
                id="standard-multiline-static"
                label="Enter Text here:"
                multiline
                sx={{
                  border: "solid",
                  borderRadius: "10px",
                  width: "400px",
                  backgroundColor: "#ffff",
                }}
                rows={10}
                // defaultValue="Default Value"
                variant="standard"
                onChange={(e) => setInput(e.target.value)}
              />
              <div style={{ display: "flex", marginTop: "10px", justifyContent: "space-between" }}>
              <Button
                component="label"
                role={undefined}
                variant="contained"
                tabIndex={-1}
                startIcon={<CloudUploadIcon />}
              >
                Upload file
                <VisuallyHiddenInput type="file" />
              </Button>
              <Button
                style={{ width: "50%" }}
                variant="contained"
                size="medium"
                onClick={() => handleAnalyze()}
              >
                Analyze
              </Button>
              </div>
              
            </div>
            <div style={{ display: "flex", flexDirection: "column" }}>
              {selectedText.key === "word_cloud" && image ? (
                <img
                  width={500}
                  height={300}
                  src={"http://127.0.0.1:5000/word_cloud_image"}
                  alt="Output"
                />
              ) : (
                <TextField
                  id="standard-multiline-static"
                  label="Output:"
                  multiline
                  sx={{
                    border: "solid",
                    borderRadius: "10px",
                    width: "400px",
                    backgroundColor: "#ffff",
                    "& .css-66dh3a-MuiInputBase-input-MuiInput-input.Mui-disabled":
                      {
                        WebkitTextFillColor: "#111827",
                      },
                  }}
                  rows={10}
                  // defaultValue="Default Value"
                  disabled
                  variant="standard"
                  value={output}
                />
              )}
              {/* <Button variant="outlined" size="medium">
                Analyze
              </Button> */}
            </div>
          </div>
        </div>
      </Main>
    </Box>
  );
}

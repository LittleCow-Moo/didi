const Discord = require("discord.js");
const client = new Discord.Client({ ws: { properties: { $browser: "Discord Android" }} }); // you can also add flags

client.on("ready", ()=>{
  console.log("bot is ready!");
})

client.login(null); // change it to the bot's token :)

package main

/*
 * Browser Automation using GOlang
 * Instagram Version
 */

import (
	"fmt"

	"github.com/tebeka/selenium"
	"github.com/tebeka/selenium/firefox"
)

func main() {
	caps := selenium.Capabilities{"browserName": "firefox"}
	firecaps := firefox.Capabilities{
		Args: []string{
			"--headless",
			"--no-sandbox",
			"--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7",
		},
	}
	caps.AddFirefox(firecaps)
	wd, err := selenium.NewRemote(caps, "https://instagram.com")
	fmt.Printf("%v\n%v\n", wd, err)
}

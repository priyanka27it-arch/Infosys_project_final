import {Fragment,useEffect} from "react"
import {Container as RadixThemesContainer,Heading as RadixThemesHeading,Text as RadixThemesText} from "@radix-ui/themes"
import {jsx} from "@emotion/react"





export default function Component() {





  return (
    jsx(Fragment,{},jsx(RadixThemesContainer,{css:({ ["padding"] : "16px" }),size:"3"},jsx(RadixThemesHeading,{},"Chat Page"),jsx(RadixThemesText,{as:"p"},"Ask questions about your documents")),jsx("title",{},"InfosysProject | Chat"),jsx("meta",{content:"favicon.ico",property:"og:image"},))
  )
}
import {Fragment,useEffect} from "react"
import {Container as RadixThemesContainer,Heading as RadixThemesHeading,Text as RadixThemesText} from "@radix-ui/themes"
import {jsx} from "@emotion/react"





export default function Component() {





  return (
    jsx(Fragment,{},jsx(RadixThemesContainer,{css:({ ["padding"] : "16px" }),size:"3"},jsx(RadixThemesHeading,{},"Upload Page"),jsx(RadixThemesText,{as:"p"},"Upload your documents here")),jsx("title",{},"InfosysProject | Upload"),jsx("meta",{content:"favicon.ico",property:"og:image"},))
  )
}
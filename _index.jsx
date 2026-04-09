import {Fragment,useEffect} from "react"
import {Container as RadixThemesContainer,Heading as RadixThemesHeading,Text as RadixThemesText} from "@radix-ui/themes"
import {jsx} from "@emotion/react"





export default function Component() {





  return (
    jsx(Fragment,{},jsx(RadixThemesContainer,{css:({ ["padding"] : "16px" }),size:"3"},jsx(RadixThemesHeading,{},"AI Document Chatbot"),jsx(RadixThemesText,{as:"p"},"Upload documents and chat with them!")),jsx("title",{},"InfosysProject | Index"),jsx("meta",{content:"favicon.ico",property:"og:image"},))
  )
}
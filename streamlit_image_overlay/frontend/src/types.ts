import type { FrontendState } from "@streamlit/component-v2-lib";
import type { CSSProperties } from "react";


// Data types

export interface CircleOverlay {
    id: string;
    type: "circle";
    data: {
        x: number;
        y: number;
        radius: number;
    };
    tooltip: string;
}


export type Overlay = CircleOverlay;


export interface TooltipPosition {
    x: number;
    y: number;
}


export interface ComponentStyles {
    tooltip?: CSSProperties;
    viewport?: CSSProperties;
    circle?: CSSProperties;
    //contour?: CSSProperties;
}


export interface OverlayState extends FrontendState {
}


export interface OverlayData {
     image: {
        src: string;
        width: number;
        height: number;
    };
    overlays: Overlay[];
    styles: ComponentStyles;
}



// Default styles

export const tooltipStyle = {
    position: "absolute" as const,
    textAlign: "left" as const,
    whiteSpace: "nowrap" as const,
    userSelect: "none" as const,
    background: "white",
    color: "black",
    border: "1px solid #888",
    borderRadius: "4px",
    padding: "6px 8px",
    fontSize: "12px",
    lineHeight: "1.15",
    boxShadow: "0 2px 6px rgba(0,0,0,0.5)",
    pointerEvents: "none" as const,
    zIndex: 1000
}


export const viewportStyle = {
    position: "relative" as const,
    width: "100%",
    height: "85vh",
    overflow: "hidden" as const,
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    userSelect: "none" as const,
    overscrollBehavior: "contain" as const,
    touchAction: "none" as const,
    border: "1px solid #fff",
    outline: "1px solid #000",
}
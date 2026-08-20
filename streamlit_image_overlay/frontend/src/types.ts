import type { FrontendState } from "@streamlit/component-v2-lib";
import type { CSSProperties } from "react";


// Data types

export interface CircleOverlay {
    id: string;
    type: "circle";
    class: string;
    data: {
        x: number;
        y: number;
        radius: number;
    };
    tooltip?: string;
}


export interface PathOverlay {
    id: string
    type: "path"
    class: string;
    data: {
        d: string;
    }
    tooltip?: string;
}


export type Overlay =
    | CircleOverlay
    | PathOverlay


export interface TooltipPosition {
    x: number;
    y: number;
}


export interface OverlayStyles {
    default?: CSSProperties;
    class?: Record<string, CSSProperties>;
    hover?: CSSProperties;
}


export interface ComponentStyles {
    tooltip?: CSSProperties;
    help?: CSSProperties;
    viewport?: CSSProperties;
    circle?: OverlayStyles;
    path?: OverlayStyles;
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
    showHelp: boolean;
}



// Default styles

export const defaultHoverStyle = {
    strokeWidth: 2,
    fill: "rgba(255, 255, 255, 0.1)",
}


export const defaultOverlayStyle = {
    fill: "rgba(255, 255, 255, 0)",
    stroke: "white",
    strokeWidth: 1,
}


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
    height: "100%",
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


export const helpIconStyle = {
    position: "absolute" as const,
    top: "8px",
    right: "8px",
    zIndex: 10,
    cursor: "help",
    color: "white",
    fontSize: "16px",
    lineHeight: 1,
}


export const helpStyle = {
    position: "absolute" as const,
    right: 0,
    top: "24px",
    minWidth: "180px",
    whiteSpace: "pre-line",
    background: "black",
    color: "white",
    borderRadius: "6px",
    padding: "8px 10px",
    fontSize: "12px",
    lineHeight: "1.4",
    boxShadow: "0 2px 6px rgba(0,0,0,0.4)",
}

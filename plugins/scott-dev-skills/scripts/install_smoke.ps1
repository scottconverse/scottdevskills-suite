param(
  [string]$CodexExe = "$env:LOCALAPPDATA\OpenAI\Codex\bin\f1c7ee7a13db5fed\codex.exe",
  [string]$MarketplaceSource = "scottconverse/scottdevskills-suite",
  [AllowEmptyString()]
  [string]$Ref = "main",
  [AllowEmptyString()]
  [string]$SparsePath = "plugins/scott-dev-skills",
  [string]$BaseDir = "C:\dev\scottdevskills-install-smoke",
  [switch]$KeepHomes
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path -LiteralPath $CodexExe)) {
  $codexCommand = Get-Command codex -ErrorAction SilentlyContinue
  if ($codexCommand) {
    $CodexExe = $codexCommand.Source
  } else {
    throw "Codex executable not found. Pass -CodexExe with the full path."
  }
}

function Invoke-Codex {
  param(
    [Parameter(Mandatory = $true)][string[]]$Args,
    [Parameter(Mandatory = $true)][string]$CodexHome
  )

  $previous = $env:CODEX_HOME
  try {
    $env:CODEX_HOME = $CodexHome
    & $CodexExe @Args
    if ($LASTEXITCODE -ne 0) {
      throw "Codex command failed with exit code $LASTEXITCODE"
    }
  } finally {
    $env:CODEX_HOME = $previous
  }
}

function Add-Marketplace {
  param([string]$CodexHome)

  $args = @("plugin", "marketplace", "add", $MarketplaceSource, "--json")
  if (-not [string]::IsNullOrWhiteSpace($Ref)) {
    $args += @("--ref", $Ref)
  }
  if (-not [string]::IsNullOrWhiteSpace($SparsePath)) {
    $args += @("--sparse", $SparsePath)
  }
  Invoke-Codex -Args $args -CodexHome $CodexHome
}

function Test-Home {
  param([string]$CodexHome)

  if (Test-Path -LiteralPath $CodexHome) {
    Remove-Item -LiteralPath $CodexHome -Recurse -Force
  }
  New-Item -ItemType Directory -Path $CodexHome | Out-Null
  Add-Marketplace -CodexHome $CodexHome
  Invoke-Codex -Args @("plugin", "add", "scott-dev-skills@scottdevskills", "--json") -CodexHome $CodexHome
  Invoke-Codex -Args @("plugin", "list", "--json") -CodexHome $CodexHome
}

$shortHome = Join-Path $BaseDir "short-home"
$longSegment = "long-path-" + ("x" * 96)
$longHome = Join-Path $BaseDir $longSegment

try {
  Test-Home -CodexHome $shortHome
  Test-Home -CodexHome $longHome
  Write-Output "install_smoke: PASS"
} finally {
  if (-not $KeepHomes) {
    foreach ($codexHomePath in @($shortHome, $longHome)) {
      if (Test-Path -LiteralPath $codexHomePath) {
        Remove-Item -LiteralPath $codexHomePath -Recurse -Force
      }
    }
  }
}
